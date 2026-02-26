from nicegui import ui
from config.settings import GREEN, RED

def render_sidebar(open_state):
    """Sidebar avec profil + menu."""
    with ui.column().classes('bg-white shadow-lg w-64 p-4 gap-4 h-screen'):
        # Profil
        ui.image('/static/logo_powermind.png').classes('h-16 w-auto')
        ui.label('John Doe').classes('text-xl font-bold')
        ui.label('john@example.com').classes('text-sm text-gray-500')
        
        # Menu
        ui.button('🏠 Home', on_click=lambda: ui.navigate.to('/dashboard')).classes('w-full')
        ui.button('📊 Consommation', on_click=lambda: ui.navigate.to('/dashboard/consommation'))
        # ... autres
        ui.button('🚪 Déconnexion', color=RED).classes('w-full mt-auto')
