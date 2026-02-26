from nicegui import ui, app
from components.layout import create_dashboard_layout

GREEN = '#27ae60'
RED = '#e74c3c'
GRAY = '#7f8c8d'
# Fichiers statiques
app.add_static_files('/assets', 'static')

from nicegui import ui
from components.layout import create_dashboard_layout

# ----- CONTENU PAGES -----
def home_content():
    """Page Home."""
    ui.label(' BIENVENUE SUR VOTRE DASHBOARD SUIVI4K !').classes('text-4xl font-bold text-center text-gray-800 mb-12')
    ui.label("Sélectionnez une option dans la barre latérale").classes('text-2xl text-center text-gray-500')

def profil_content():
    """Page Modifier Profil."""
    ui.label(' MODIFIER PROFIL').classes('text-4xl font-bold text-blue-600 mb-8')
    with ui.card().classes('p-8 shadow-xl rounded-3xl max-w-2xl mx-auto'):
        with ui.column().classes('gap-6 w-full'):
            ui.input('Nom complet', value='Jean Dupont').classes('w-full text-xl py-3').props('outlined')
            ui.input('Email', value='jean.dupont@email.com').classes('w-full text-xl py-3').props('outlined')
            ui.input('Nouveau mot de passe', password=True).classes('w-full text-xl py-3').props('outlined')
            ui.input('Confirmer mot de passe', password=True).classes('w-full text-xl py-3').props('outlined')
            ui.button(' SAUVEGARDER', color='green').classes('w-full text-xl py-4 rounded-2xl shadow-xl')

def modif_content():
    """Page Modifier Heure/Date."""
    ui.label(' MODIFIER HEURE ET DATE').classes('text-4xl font-bold text-yellow-600 mb-8')
    with ui.card().classes('p-8 shadow-xl rounded-3xl max-w-lg mx-auto'):
        ui.date('Nouvelle date').classes('w-full mb-6').props('outlined')
        ui.time('Nouvelle heure').classes('w-full mb-6').props('outlined')
        ui.button(' SYNCHRONISER', color='blue').classes('w-full text-xl py-4 rounded-2xl shadow-xl')

def base_content():
    """Page Valeurs de Base + Capteurs."""
    ui.label(' VALEURS DE BASE & CAPTEURS').classes('text-4xl font-bold text-purple-600 mb-8')
    
    # 3 CAPTEURS
    with ui.row().classes('gap-8 w-full'):
        # TEMPÉRATURE
        with ui.card().classes('flex-1 p-8 shadow-xl rounded-3xl border-4 border-green-200'):
            ui.icon('thermostat').classes('text-6xl text-green-500 mx-auto mb-4')
            ui.label('24.5°C').classes('text-5xl font-black text-green-600 text-center')
            ui.label('Seuil: 28°C max').classes('text-xl text-gray-500 text-center')
            ui.label('✅ OK').classes('text-2xl font-bold text-green-700 text-center mt-2')
        # HUMIDITÉ
        with ui.card().classes('flex-1 p-8 shadow-xl rounded-3xl border-4 border-blue-200'):
            ui.icon('humidity').classes('text-6xl text-blue-500 mx-auto mb-4')
            ui.label('68%').classes('text-5xl font-black text-blue-600 text-center')
            ui.label('Seuil: 75% max').classes('text-xl text-gray-500 text-center')
            ui.label('✅ OK').classes('text-2xl font-bold text-blue-700 text-center mt-2')
        # MOUVEMENT
        with ui.card().classes('flex-1 p-8 shadow-xl rounded-3xl border-4 border-orange-200'):
            ui.icon('motion_sensor_active').classes('text-6xl text-orange-500 mx-auto mb-4')
            ui.label('ACTIF').classes('text-5xl font-black text-orange-600 text-center')
            ui.label("Dernière: 11:42").classes('text-xl text-gray-500 text-center')
            ui.label(' Surveillance').classes('text-2xl font-bold text-orange-700 text-center mt-2')

# ----- PAGES PRINCIPALES -----
@ui.page('/dashboard')
def dashboard_page():
    ui.page_title('SUIVI4K - Dashboard')
    create_dashboard_layout(' Dashboard Home', home_content)

@ui.page('/dashboard/home')
def dashboard_home():
    create_dashboard_layout(' Home', home_content)

@ui.page('/dashboard/profil')
def dashboard_profil():
    create_dashboard_layout(' Modifier Profil', profil_content)

@ui.page('/dashboard/modif')
def dashboard_modif():
    create_dashboard_layout(' Modifier Heure/Date', modif_content)

@ui.page('/dashboard/base')
def dashboard_base():
    create_dashboard_layout(' Valeurs de Base', base_content)