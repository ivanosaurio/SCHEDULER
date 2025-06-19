import flet as ft
from theme import BACKGROUND, APP_THEME
from views.dashboard_view import DashboardView

async def main (page: ft.Page):
    page.title = "Social Scheduler"
    page.bgcolor = BACKGROUND
    page.theme = APP_THEME
    page.clean()
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.START
    
    app_layout = DashboardView(page)
    page.add(app_layout)

if __name__ == "__main__":
    ft.app(target=main)