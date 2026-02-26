from nicegui import ui, app
from components.layout import create_dashboard_layout

GREEN = '#27ae60'
RED = '#e74c3c'
GRAY = '#7f8c8d'
# Fichiers statiques
app.add_static_files('/assets', 'static')

# ----- PAGE PRINCIPALE -----
@ui.page('/dashboard')
def dashboard_page():
    ui.page_title('SUIVI4K - Dashboard')
    create_dashboard_layout('Dashboard')


# ----- SOUS-PAGES -----
@ui.page('/dashboard/home')
def dashboard_home():
    create_dashboard_layout(' Accueil')


@ui.page('/dashboard/profil')
def dashboard_profil():
    create_dashboard_layout(' Modifier profil')


@ui.page('/dashboard/heure')
def dashboard_heure():
    create_dashboard_layout(' Modifier heure et date')


@ui.page('/dashboard/valeurs')
def dashboard_valeurs():
    create_dashboard_layout(' Valeurs de bases')

@ui.page('/connexion')
def dashboard_deconnexion():
    create_dashboard_layout(' Déconnexion')