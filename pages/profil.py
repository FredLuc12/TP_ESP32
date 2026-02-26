from nicegui import ui
from components.layout import create_dashboard_layout

def profil_content():
    """Contenu page Modifier Profil."""
    with ui.column().classes('gap-8 w-full max-w-2xl mx-auto'):
        ui.label('Modification du profil').classes('text-3xl text-gray-700')
        # Formulaire profil
        with ui.card().classes('p-8 shadow-xl rounded-3xl'):
            with ui.column().classes('gap-6'):
                ui.input('Nom complet', value='Jean Dupont').classes('w-full text-xl').props('outlined')
                ui.input('Email', value='jean.dupont@email.com').classes('w-full text-xl').props('outlined')
                ui.input('Nouveau mot de passe').classes('w-full text-xl').props('outlined password')
                ui.input('Confirmer mot de passe').classes('w-full text-xl').props('outlined password')
                ui.button('Sauvegarder', color='green').classes('w-full text-xl py-4 rounded-2xl shadow-xl')
@ui.page('/profil')
def dashboard_profil():
    create_dashboard_layout(' Modifier Profil', profil_content)