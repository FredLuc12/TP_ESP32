from nicegui import ui, app
from config.settings import STATIC_PATH
from pages.accueil import accueil_page
from pages.connexion import connexion_page
from pages.dashboard import dashboard_page, dashboard_home, dashboard_consommation, dashboard_heure, dashboard_valeurs, dashboard_deconnexion
# Import toutes les pages...

app.add_static_files('/static', STATIC_PATH)  # Assets [web:24]

ui.page('/')(accueil_page)
ui.page('/connexion')(connexion_page)
ui.page('/dashboard')(dashboard_page)
ui.page('/dashboard/home')(dashboard_home)
ui.page('/dashboard/consommation')(dashboard_consommation)
ui.page('/dashboard/heure')(dashboard_heure)
ui.page('/dashboard/valeurs')(dashboard_valeurs)
ui.page('/dashboard/deconnexion')(dashboard_deconnexion)
# ... autres pages

if __name__ in {'__main__', '__mp_main__'}:
    ui.run(title='SUIVI4K UI', reload=True)  # Dev mode [web:31]