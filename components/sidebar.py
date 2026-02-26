from nicegui import ui
from config.settings import GREEN  # À créer si pas fait

def render_sidebar(drawer, title):
    drawer = ui.left_drawer().classes('bg-white shadow-xl w-72')

    # Bouton hamburger
    ui.button(
        '☰',
        on_click=lambda: drawer.toggle()
    ).classes(
        'fixed top-4 left-4 z-50 bg-white shadow-lg rounded-full w-12 h-12 text-xl'
    )

    # Contenu du drawer
    with drawer:
        with ui.column().classes('p-6 gap-6 h-full'):

            # Profil
            with ui.row().classes('items-center gap-3 mb-6 p-4 bg-gray-50 rounded-2xl'):
                ui.image('/assets/profil.webp').classes(
                    'w-14 h-14 rounded-full border-2 border-green-200'
                )
                with ui.column().classes('gap-1'):
                    ui.label('Jean Dupont').classes(
                        'text-lg font-bold text-gray-900'
                    )
                    ui.label('jean.dupont@email.com').classes(
                        'text-sm text-gray-500'
                    )
            # Menu
            nav_items = [
                ('Home', '/dashboard/home'),
                ('Consommation', '/dashboard/consommation'),
                ('Modifier heure et date', '/dashboard/heure'),
                ('Valeurs de bases', '/dashboard/valeurs'),
                ('Deconnexion', '/connexion')
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

            ui.button(
                ' Déconnexion',
                on_click=lambda: ui.navigate.to('/')
            ).classes(
                'w-full text-left py-3 px-4 rounded-xl '
                'bg-red-50 hover:bg-red-100 border-l-4 border-red-500 shadow-sm'
            )

    # Contenu principal
    with ui.column().classes('p-6 pt-20 gap-8'):
        ui.label(title).classes('text-3xl font-bold text-gray-900')
        ui.label('Contenu de cette section...').classes(
            'text-gray-500 text-lg'
        )