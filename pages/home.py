from nicegui import ui
from components.layout import create_dashboard_layout

def home_content():
    """Contenu page Home."""
    with ui.column().classes('gap-8 w-full'):
        ui.label('Bienvenue dans votre dashboard SUIVI4K !').classes('text-3xl text-gray-700 font-light')
        
        # Cards rapides
        with ui.row().classes('gap-6 w-full'):
            with ui.card().classes('flex-1 p-8 shadow-xl rounded-3xl'):
                ui.icon('dashboard', color='green').classes('text-5xl mx-auto mb-4')
                ui.label('Statut Global').classes('text-3xl font-bold text-center text-green-600')
                ui.label('Tous systèmes OK').classes('text-xl text-center text-green-800')
            with ui.card().classes('flex-1 p-8 shadow-xl rounded-3xl'):
                ui.icon('notifications', color='orange').classes('text-5xl mx-auto mb-4')
                ui.label('Alertes').classes('text-3xl font-bold text-center text-orange-600')
                ui.label('0 actif').classes('text-xl text-center text-orange-800')

@ui.page('/dashboard/home')
def home_page():
    create_dashboard_layout(' Dashboard Home', home_content)
