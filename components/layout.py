from nicegui import ui
from components.sidebar import render_sidebar

# ----- LAYOUT COMMUN -----
def create_dashboard_layout(title: str):
    """Layout dashboard avec sidebar + contenu principal."""
    # 1. Sidebar (drawer)
    drawer = ui.left_drawer().classes('bg-white shadow-xl w-72')
    # 2. Bouton hamburger (fixe en haut à gauche)
    ui.button(
        '☰',
        on_click=lambda: drawer.toggle()
    ).classes(
        'fixed top-4 left-4 z-50 bg-white shadow-lg rounded-full w-12 h-12 text-xl'
    )
    # 3. Contenu de la sidebar
    with drawer:
        with ui.column().classes('p-6 gap-6 h-full'):
            render_sidebar(drawer)  # ← Composant réutilisable

    # 4. Contenu principal (à droite)
    with ui.column().classes('p-6 pt-20 gap-8'):  # pt-20 = décalage pour hamburger
        ui.label(title).classes('text-3xl font-bold text-gray-900')
        ui.label('Contenu de cette section...').classes('text-gray-500 text-lg')

class DashboardSidebar(ui.left_drawer):
    """Sidebar réutilisable pour les pages du dashboard."""
    def __init__(self):
        super().__init__()
        self.classes('bg-white shadow-xl w-72')
        self.render_content()
    def render_content(self):
        """Rendu du contenu de la sidebar (profil + menu)."""
        # Profil utilisateur
        with ui.row().classes('items-center gap-3 mb-6 p-4 bg-gray-50 rounded-2xl'):
            ui.image('/assets/profil.webp').classes(
                'w-14 h-14 rounded-full border-2 border-green-200'
            )
            with ui.column().classes('gap-1'):
                ui.label('Jean Dupont').classes('text-lg font-bold text-gray-900')
                ui.label('jean.dupont@email.com').classes('text-sm text-gray-500')