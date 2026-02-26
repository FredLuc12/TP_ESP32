from nicegui import ui

from components.layout import create_dashboard_layout

def base_content():
    """Contenu page Valeurs de base + Alertes."""
    with ui.column().classes('gap-8 w-full'):
        ui.label(' VALEURS DE BASE & ALERTES').classes('text-3xl text-gray-700')
        # 3 CAPTEURS avec seuils + alertes
        with ui.row().classes('gap-8 w-full'):
            # TEMPÉRATURE & HUMIDITÉ
            with ui.card().classes('flex-1 p-8 shadow-xl rounded-3xl border-4 border-green-200'):
                ui.label(' TEMPÉRATURE & HUMIDITÉ').classes('text-2xl font-bold text-green-800 mb-6')
                ui.label('24.5°C | 68%').classes('text-5xl font-black text-green-600 mb-2')
                ui.label('Seuil max : 28°C | 75%').classes('text-xl text-gray-500')
                ui.label(' Dans les seuils').classes('text-lg font-semibold text-green-700 mt-4')

            # MOUVEMENT
            with ui.card().classes('flex-1 p-8 shadow-xl rounded-3xl border-4 border-orange-200'):
                ui.label(' DÉTECTEUR MOUVEMENT').classes('text-2xl font-bold text-orange-800 mb-6')
                ui.label('ACTIF').classes('text-5xl font-black text-orange-600 mb-2')
                ui.label("Dernière détection : 11:42").classes('text-xl text-gray-500')
                ui.label(' Surveillance active').classes('text-lg font-semibold text-orange-700 mt-4')
        # HISTORIQUE ALERTES
        with ui.card().classes('p-8 shadow-2xl rounded-3xl w-full'):
            ui.label(' ALERTES RECENTES').classes('text-2xl font-bold text-red-800 mb-6')
            with ui.table(columns=[
                {'name': 'date', 'label': 'Date', 'field': 'date'},
                {'name': 'capteur', 'label': 'Capteur', 'field': 'capteur'},
                {'name': 'valeur', 'label': 'Valeur', 'field': 'valeur'},
                {'name': 'statut', 'label': 'Statut', 'field': 'statut'},
            ], rows=[
                {'date': '11:42', 'capteur': 'Mouvement', 'valeur': 'ACTIF', 'statut': 'Résolu'},
            ]).classes('w-full').props('dense'):
                pass
            ui.button('Envoyer test alerte', color='red').classes('mt-4 text-xl py-3 px-8 rounded-xl shadow-xl')
@ui.page('/base')
def dashboard_base():
    create_dashboard_layout('Valeurs', base_content)