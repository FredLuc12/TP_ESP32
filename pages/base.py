from nicegui import ui
from database import get_connection
from pages.connexion import user_session
from components.layout import create_dashboard_layout
from webhook import send_make_webhook

def base_content():
    """Contenu page Valeurs de base + Alertes depuis BDD."""
    with ui.column().classes('gap-6 w-full'):

        # Seuils utilisateur (BDD)
        if not user_session['user_id']:
            ui.label('Connectez-vous pour voir vos données').classes('text-xl text-red-600 text-center p-6')
            return
        
        try:
            conn = get_connection()
            cursor = conn.cursor()
            
            # Seuils utilisateur (table thresholds)
            cursor.execute("SELECT temp_max, humidite_max, mouvement_actif FROM thresholds WHERE id=1")
            seuils = cursor.fetchone()
            
            # Dernières données capteurs
            cursor.execute("""
                SELECT temperature, humidite, mouvement, created_at 
                FROM sensor_data 
                ORDER BY created_at DESC 
                LIMIT 1
            """)
            dernier_capteur = cursor.fetchone()

            # Alertes récentes utilisateur
            cursor.execute("""
                SELECT a.type_alerte, a.message, a.created_at, a.resolved
                FROM alerts a
                ORDER BY a.created_at DESC
                LIMIT 5
            """)
            alertes_raw = cursor.fetchall()
            alertes = [dict(row) for row in alertes_raw]
            conn.close()
        except:
            seuils = (28.0, 75.0, 1)
            dernier_capteur = (24.5, 68.0, 1, '26-02-27 10:15')
            alertes = []
        
        temp_max, humid_max, mouvement_actif = seuils or (28.0, 75.0, 1)
        temp, humid, mouvement, timestamp = dernier_capteur or (24.5, 68.0, 1, 'Maintenant')
        
        
        def check_and_send_alert(temp, humid, temp_max, humid_max):
            """Vérifie seuils et envoie webhook si dépassé."""
            en_alerte = False
            
            if temp > temp_max:
                send_make_webhook("temperature", temp, temp_max, f"Température dépasse {temp_max}°C")
                en_alerte = True
            
            if humid > humid_max:
                send_make_webhook("humidite", humid, humid_max, f"Humidité dépasse {humid_max}%")
                en_alerte = True

            return en_alerte

        if check_and_send_alert(temp, humid, temp_max, humid_max):
                ui.notify("Nouvelle alerte envoyée !", color='negative', position='top')
        # 3 CAPTEURS (taille RÉDUITE)
        with ui.row().classes('gap-6 w-full'):
            # TEMPÉRATURE
            with ui.card().classes('flex-1 p-6 shadow-lg rounded-2xl border-2 border-green-100'):
                ui.label(' TEMPÉRATURE').classes('text-lg font-bold text-green-700 mb-3')
                ui.label(f'{temp:.1f}°C').classes('text-3xl font-black text-green-600 mb-1')
                ui.label(f'Seuil: {temp_max}°C').classes('text-sm text-gray-500')
                status = 'OK' if temp <= temp_max else ' ALERTE'
                status_color = 'text-green-700' if temp <= temp_max else 'text-red-700'
                ui.label(status).classes(f'text-base font-semibold {status_color} mt-2')
            
            # HUMIDITÉ
            with ui.card().classes('flex-1 p-6 shadow-lg rounded-2xl border-2 border-blue-100'):
                ui.label('HUMIDITÉ').classes('text-lg font-bold text-blue-700 mb-3')
                ui.label(f'{humid:.0f}%').classes('text-3xl font-black text-blue-600 mb-1')
                ui.label(f'Seuil: {humid_max}%').classes('text-sm text-gray-500')
                status = 'OK' if humid <= humid_max else 'ALERTE'
                status_color = 'text-blue-700' if humid <= humid_max else 'text-red-700'
                ui.label(status).classes(f'text-base font-semibold {status_color} mt-2')

            # MOUVEMENT
            with ui.card().classes('flex-1 p-6 shadow-lg rounded-2xl border-2 border-orange-100'):
                ui.label('MOUVEMENT').classes('text-lg font-bold text-orange-700 mb-3')
                status_mvt = 'ACTIF' if mouvement else 'INACTIF'
                ui.label(status_mvt).classes('text-3xl font-black text-orange-600 mb-1')
                ui.label(f'Dernière: {timestamp[:16]}').classes('text-sm text-gray-500')
                ui.label('Surveillance').classes('text-base font-semibold text-orange-700 mt-2')
        
        # ALERTES TABLE CORRIGÉE
        with ui.card().classes('p-6 shadow-xl rounded-2xl w-full'):
            ui.label('ALERTES RÉCENTES').classes('text-lg font-bold text-red-700 mb-4')
            
            # DEBUG : Affiche nombre alertes
            ui.label(f'Résultats: {len(alertes)} alertes trouvées').classes('text-sm text-gray-600 mb-2')
            
            if not alertes:
                ui.label('Aucune alerte récente').classes('text-gray-500 text-center py-8 italic')
            else:
                ui.table(
                    columns=[
                        {'name': 'created_at', 'label': 'Date', 'field': 'created_at'},
                        {'name': 'type_alerte', 'label': 'Capteur', 'field': 'type_alerte'},
                        {'name': 'message', 'label': 'Message', 'field': 'message'},
                    ],
                    rows=[
                        {
                            'created_at': dict(alerte)['created_at'][:16] if dict(alerte).get('created_at') else 'N/A',
                            'type_alerte': dict(alerte).get('type_alerte', 'Inconnu'),
                            'message': dict(alerte).get('message', 'Pas de message')
                        }
                        for alerte in alertes
                    ]
                ).classes('w-full').props('dense')
        ui.button(' Test alerte', color='red').classes('mt-4 text-base py-2 px-6 rounded-xl shadow-md').on('click', lambda: check_and_send_alert(30.5, 80, temp_max, humid_max))
@ui.page('/dashboard/base')
def dashboard_base():
    ui.page_title('SUIVI4K - Capteurs')
    create_dashboard_layout('Valeurs de Base', base_content)
