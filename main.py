from nicegui import ui, app
from models import create_tables

create_tables()
# Assets statiques
app.add_static_files('/assets', 'static')  # ← Garde /assets comme tu l'utilises

# Imports pages
from pages.accueil import accueil_page
from pages.connexion import connexion_page
from pages.home import dashboard_home
from pages.base import dashboard_base
from pages.modif import dashboard_modif
from pages.profil import dashboard_profil
from pages.dashboard import (
    dashboard_page
)

# Routes principales
ui.page('/')(accueil_page)
ui.page('/connexion')(connexion_page)
ui.page('/dashboard')(dashboard_page)           # Dashboard par défaut
ui.page('/home')(dashboard_home)      # Home
ui.page('/profil')(dashboard_profil)  # Profil
ui.page('/modif')(dashboard_modif)    # Heure/Date
ui.page('/base')(dashboard_base)      # Capteurs

if __name__ in {'__main__', '__mp_main__'}:
    ui.run(
        host='127.0.0.1',
        port=8081,
        reload=True,
        show=True,
        title='SUIVI4K Dashboard'
    )