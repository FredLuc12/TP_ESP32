from nicegui import ui
from components.layout import create_dashboard_layout
from datetime import datetime

def modif_content():
    """Contenu page Modifier Heure/Date."""
    with ui.column().classes('gap-8 w-full max-w-lg mx-auto'):
        ui.label('Modifier heure et date système').classes('text-3xl text-gray-700')
        
        with ui.card().classes('p-8 shadow-xl rounded-3xl'):
            with ui.column().classes('gap-6'):
                # Date actuelle
                current_date = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
                ui.label(f'Date actuelle : {current_date}').classes('text-xl text-gray-500 p-4 bg-gray-50 rounded-xl')
                # Sélecteurs
                ui.date('Nouvelle date').classes('w-full').props('outlined')
                ui.time('Nouvelle heure').classes('w-full').props('outlined')
                ui.button('🔄 Synchroniser', color='blue').classes('w-full text-xl py-4 rounded-2xl shadow-xl')

@ui.page('/dashboard/modif')
def modif_page():
    create_dashboard_layout(' Modifier Heure/Date', modif_content)
