from nicegui import ui

GREEN = '#27ae60'
RED = '#e74c3c'
GRAY = '#7f8c8d'

@ui.page('/connexion')
def connexion_page():
    ui.page_title('SUIVI4K - Connexion')

    with ui.column().classes('min-h-screen items-center justify-center bg-grey-1 py-8'):
        with ui.card().classes('w-full max-w-sm p-8 shadow-xl'):
            with ui.column().classes('gap-6 items-center'):

                # ----- TITRE -----
                ui.label('Connexion').style(
                    f'color: {GREEN}; font-size: 2.5rem; font-weight: 700;'
                )

                # ----- FORMULAIRE -----
                with ui.card().classes('w-full p-6 shadow-inner'):
                    ui.input('Identifiant', value='').classes('w-full').props('dense outlined')
                    ui.input('Mot de passe', value='', password=True).classes('w-full').props('dense outlined')

                # ----- BOUTON IDENTIFICATION -----
                ui.button(
                    'S\'identifier',
                    color=RED,
                    on_click=lambda: ui.navigate.to('/dashboard')  # ← ALLER vers DASHBOARD
                ).classes('w-full py-3 text-white font-semibold rounded-lg mt-4')

                # ----- LIEN CRÉATION COMPTE -----
                ui.label("Je souhaite créer un compte").style(
                    f'color: {GRAY}; font-size: 0.8rem; cursor: pointer;'
                ).on('click', lambda: ui.notify('Création de compte bientôt disponible'))
