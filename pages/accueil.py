from nicegui import ui
from config.settings import GREEN, RED, GRAY
from pages.connexion import connexion_page  # Pas besoin, navigation via ui.navigate

def accueil_page():
    """Page d'accueil Suivi - Logo + 3 boutons d'action responsive."""
    ui.page_title('SUIVI4K - Accueil')
    # ----- LAYOUT DASHBOARD -----
    # Layout global centré + responsive
    with ui.column().classes('min-h-screen items-center justify-center gap-8 p-4 bg-gradient-to-br from-gray-50 to-blue-50'):
        # Logo principal
        ui.image('/static/logo.png').classes('h-48 w-auto shadow-2xl rounded-xl')
        # Titre app
        ui.label('SUIVI4K').classes('text-5xl font-black text-gray-800 drop-shadow-lg')
        # 3 indicateurs (date/heure + temp, statiques pour l'instant)
        with ui.row().classes('w-full max-w-md gap-4'):
            with ui.card().classes('flex-1 p-4 bg-white shadow-lg rounded-xl text-center'):
                ui.label('26/02/2026').classes('text-2xl font-bold text-gray-700')
                ui.label('09:43').classes('text-lg text-gray-500')
            with ui.card().classes('flex-1 p-4 bg-white shadow-lg rounded-xl text-center'):
                ui.label('24°C').classes('text-2xl font-bold text-blue-600')
                ui.label('Eau').classes('text-sm text-gray-500 uppercase')
            with ui.card().classes('flex-1 p-4 bg-white shadow-lg rounded-xl text-center'):
                ui.label('22°C').classes('text-2xl font-bold text-green-600')
                ui.label('Air').classes('text-sm text-gray-500 uppercase')
        # 3 boutons d'action (vers connexion)
        with ui.column().classes('gap-4 w-full max-w-md'):
            ui.button(
                ' Démarrer',
                color=GREEN,
                size='lg',
                on_click=lambda: ui.navigate.to('/connexion')
            ).classes('text-xl font-semibold shadow-xl hover:shadow-2xl')
            ui.button(
                'Paramètres',
                color=GRAY,
                size='lg',
                on_click=lambda: ui.navigate.to('/connexion')
            ).classes('text-xl font-semibold shadow-xl hover:shadow-2xl')
            ui.button(
                ' Alimentation',
                color=RED,
                size='lg',
                on_click=lambda: ui.navigate.to('/connexion')
            ).classes('text-xl font-semibold shadow-xl hover:shadow-2xl')
        # Lien création compte (gris discret)
        ui.link(
            'Créer un compte',
            target='/connexion'
        ).classes('text-sm hover:underline').style(f'color: {GRAY}')

# Test direct (optionnel)
if __name__ == '__main__':
    accueil_page()
    ui.run()
