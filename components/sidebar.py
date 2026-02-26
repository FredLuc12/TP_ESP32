from nicegui import ui

def render_sidebar(drawer):  # ← SEULEMENT drawer (pas title)
    """Rendu sidebar SEULEMENT (pas de layout)."""
    
    # Profil
    with ui.row().classes('items-center gap-3 mb-6 p-4 bg-gray-50 rounded-2xl'):
        ui.image('/assets/profil.webp').classes(
            'w-14 h-14 rounded-full border-2 border-green-200'
        )
        with ui.column().classes('gap-1'):
            ui.label('Jean Dupont').classes('text-lg font-bold text-gray-900')
            ui.label('jean.dupont@email.com').classes('text-sm text-gray-500')
    # Menu
    nav_items = [
        (' Home', '/dashboard/home'),
        (' Modifier profil', '/dashboard/profil'),
        (' Modifier heure et date', '/dashboard/heure'),
        (' Valeurs de bases', '/dashboard/valeurs'),
    ]
    for label, route in nav_items:
        ui.button(
            label,
            on_click=lambda r=route: [
                drawer.close(),
                ui.navigate.to(r)
            ]
        ).classes(
            'w-full justify-start text-left py-3 px-4 rounded-xl '
            'hover:bg-green-50 hover:shadow-sm transition-all '
            'border-l-4 border-transparent hover:border-green-500'
        )
    ui.separator().classes('my-6')
    # Bouton déconnexion
    ui.button(
        ' Déconnexion',
        on_click=lambda: ui.navigate.to('/connexion')
    ).classes(
        'w-full text-left py-3 px-4 rounded-xl '
        'bg-red-50 hover:bg-red-100 border-l-4 border-red-500 shadow-sm mt-auto'
    )
