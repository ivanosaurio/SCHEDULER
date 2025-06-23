import flet as ft
from theme import SURFACE, BORDER, TEXT_PRIMARY, TEXT_SECONDARY,ON_PRIMARY, PRIMARY

class Sidebar(ft.Container):
    def __init__(self, on_change, on_logout_click):
        super().__init__()
        
        self.on_change = on_change
        self.on_logout_click = on_logout_click
        self.width = 250
        self.bgcolor = SURFACE
        self.border = ft.border.only(right=ft.BorderSide(1, BORDER))
        self.padding = ft.padding.symmetric(vertical=20, horizontal=10)
        
        self.nav_buttons = {
            "Cola": self.create_nav_button(ft.Icons.LIST_ALT, "Cola", is_activate =True),
            "Analíticas": self.create_nav_button(ft.Icons.INSIGHTS, "Analíticas", is_activate =False),
            "Configuración": self.create_nav_button(ft.Icons.SETTINGS, "Configuración", is_activate =False)
        }
        
        self.logout_button = ft.Container(
            height=50,
            border_radius=8,
            padding=ft.padding.symmetric(horizontal=15),
            ink=True,
            on_hover=self.highlight_button,
            on_click=self.on_logout_click,
            content=ft.Row(
                spacing=15,
                controls=[
                    ft.Icon(ft.Icons.LOGOUT, color=TEXT_SECONDARY),
                    ft.Text(
                        "Cerrar Sesión",
                        size=14,
                        weight=ft.FontWeight.W_500, color=TEXT_SECONDARY
                        )
                ]
            )
        )
        
        self.content = ft.Column(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            expand=True,
            controls=[
                #Titulo de la APP EN LA SIDEBAR
                ft.Column(
                    spacing=10, 
                    controls=[
                        ft.Row(
                            spacing=10,
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.Icon(ft.Icons.CALENDAR_MONTH_ROUNDED, color=PRIMARY),
                                ft.Text("Social Scheduler", size=20, weight=ft.FontWeight.BOLD, color=TEXT_PRIMARY)
                                ]
                            ),
                        ft.Divider(height=25, color="transparent"),
                        *self.nav_buttons.values()
                        ]
                    ),
                self.logout_button
            ]
        )
    
    def create_nav_button(self, icon_name, text, is_activate=False):
        return ft.Container(
            height=50,
            border_radius=8,
            padding=ft.padding.symmetric(horizontal=15),
            ink=True,
            #Eventos
            on_hover=self.highlight_button,
            on_click= lambda e, view_name=text: self.handle_nav_click(view_name),
            bgcolor=PRIMARY if is_activate else "transparent",
            content= ft.Row(
                spacing=15,
                controls=[
                    ft.Icon(icon_name, color= ON_PRIMARY if is_activate else TEXT_PRIMARY),
                    ft.Text(text, size=14, weight=ft.FontWeight.W_500,color=ON_PRIMARY if is_activate else TEXT_PRIMARY)
                ]
            )
        )
    
    def set_activate(self,text):
        for name, button in self.nav_buttons.items():
            is_active = (name == text)
            button.bgcolor = PRIMARY if is_active else "transparent"
            for control in button.content.controls:
                if isinstance(control, ft.Icon):
                    control.color = ON_PRIMARY if is_active else TEXT_PRIMARY
                if isinstance(control, ft.Text):
                    control.color = ON_PRIMARY if is_active else TEXT_PRIMARY
            button.update()
    
    def handle_nav_click(self, view_name):
        self.set_activate(view_name)
        self.on_change(view_name)
    
    def highlight_button(self, e):
        if e.control.bgcolor != PRIMARY:
            e.control.bgcolor = "white10" if e.data == "true" else "transparent"
            e.control.update()