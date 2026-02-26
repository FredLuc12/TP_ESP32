from nicegui import ui

def render_sidebar(drawer):
    """Sidebar avec navigation qui MARCHE."""
    # Profil
    with ui.row().classes('items-center gap-3 mb-6 p-4 bg-gray-50 rounded-2xl'):
        ui.image('/assets/profil.webp').classes('w-14 h-14 rounded-full border-2 border-green-200')
        with ui.column().classes('gap-1'):
            ui.label('Jean Dupont').classes('text-lg font-bold text-gray-900')
            ui.label('jean.dupont@email.com').classes('text-sm text-gray-500')
    # Boutons avec LAMBDAS SIMPLES (marche À COUP SÛR)
    ui.button(
         'Home',
        on_click=lambda: [setattr(drawer, 'value', True), ui.navigate.to('/home')]
    ).classes('w-full text-left py-3 px-4 rounded-xl hover:bg-green-50 hover:shadow-sm transition-all border-l-4 border-green-500 text-lg')
    ui.button(
        'Modifier profil',
        on_click=lambda: [setattr(drawer, 'value', True), ui.navigate.to('/profil')]
    ).classes('w-full text-left py-3 px-4 rounded-xl hover:bg-blue-50 hover:shadow-sm transition-all border-l-4 border-blue-500 text-lg')
    ui.button(
        'Modifier heure et date',
        on_click=lambda: [setattr(drawer, 'value', True), ui.navigate.to('/modif')]
    ).classes('w-full text-left py-3 px-4 rounded-xl hover:bg-yellow-50 hover:shadow-sm transition-all border-l-4 border-yellow-500 text-lg')
    ui.button(
        'Valeurs de bases',
        on_click=lambda: [setattr(drawer, 'value', False), ui.navigate.to('/base')]
    ).classes('w-full text-left py-3 px-4 rounded-xl hover:bg-purple-50 hover:shadow-sm transition-all border-l-4 border-purple-500 text-lg')
    ui.separator().classes('my-6')
    ui.button(
        'Déconnexion',
        on_click=lambda: ui.navigate.to('/connexion')
    ).classes('w-full text-left py-3 px-4 rounded-xl bg-red-50 hover:bg-red-100 border-l-4 border-red-500 shadow-sm mt-auto')
