from nicegui import ui, app

# Assets statiques
app.add_static_files('/assets', 'static')  # ← Garde /assets comme tu l'utilises

# Imports pages
from pages.accueil import accueil_page
from pages.connexion import connexion_page
from pages.dashboard import (
    dashboard_page, dashboard_home, dashboard_profil,
    dashboard_modif, dashboard_base
)

# Routes principales
ui.page('/')(accueil_page)
ui.page('/connexion')(connexion_page)
ui.page('/dashboard')(dashboard_page)           # Dashboard par défaut
ui.page('/dashboard/home')(dashboard_home)      # Home
ui.page('/dashboard/profil')(dashboard_profil)  # Profil
ui.page('/dashboard/modif')(dashboard_modif)    # Heure/Date
ui.page('/dashboard/base')(dashboard_base)      # Capteurs

if __name__ in {'__main__', '__mp_main__'}:
    ui.run(
        host='127.0.0.1',
        port=8080,
        reload=True,
        show=True,
        title='SUIVI4K Dashboard'
    )