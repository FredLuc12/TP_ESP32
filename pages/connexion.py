from nicegui import ui

GREEN = '#27ae60'
RED = '#e74c3c'
GRAY = '#7f8c8d'

@ui.page('/connexion')
def connexion_page():
    ui.page_title('SUIVI4K - Connexion')

    # Layout PLEIN ÉCRAN centré
    with ui.column().classes('min-h-screen items-center justify-center bg-gradient-to-br from-gray-50 to-blue-50 py-12 px-8'):

        # CARTE CENTRALE (plus grande mais pas géante)
        with ui.card().classes('w-full max-w-2xl p-12 shadow-2xl rounded-3xl border-4 border-white/50 backdrop-blur-sm bg-white/80'):
            with ui.column().classes('gap-10 items-center w-full'):

                # LOGO + TITRE (haut de carte)
                with ui.column().classes('items-center gap-4 mb-8'):
                    ui.image('/static/logo.png').classes('h-32 w-auto shadow-xl rounded-2xl')
                    ui.label('Connexion SUIVI4K').classes('text-5xl font-black text-gray-800 drop-shadow-lg')
                    ui.label('Accédez à votre tableau de bord').classes('text-xl text-gray-500 font-light')

                # FORMULAIRE (centré + espacé)
                with ui.column().classes('w-full max-w-md gap-6'):
                    ui.input(
                        'Identifiant',
                        placeholder='jean.dupont@example.com',
                        value=''
                    ).classes('w-full text-xl py-4').props('outlined rounded-xl')

                    ui.input(
                        'Mot de passe',
                        placeholder='••••••••',
                        value='',
                        password=True
                    ).classes('w-full text-xl py-4').props('outlined rounded-xl')
                # BOUTON IDENTIFICATION (GRAND + CENTRAL)
                ui.button(
                    'S\'IDENTIFIER',
                    color=RED,
                    on_click=lambda: ui.navigate.to('/dashboard')
                ).classes('w-full text-2xl py-6 px-12 font-bold shadow-2xl hover:shadow-3xl rounded-2xl h-16 mt-4')
                # LIEN CRÉATION COMPTE
                ui.label(" Je souhaite créer un compte").classes(
                    'text-lg font-semibold hover:underline cursor-pointer mt-6 text-center'
                ).style(f'color: {GRAY}').on('click', lambda: ui.notify('Création de compte bientôt disponible'))
