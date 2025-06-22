import flet as ft
from theme import TEXT_PRIMARY, TEXT_SECONDARY

class PlaceholderView(ft.Column):
    def __init__(self, icon_name: str, title: str, message: str):
        super().__init__()
        
        self.alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.expand = True
        self.spacing = 20
        
        self.controls = [
            ft.Icon(
                name=icon_name,
                size=80, 
                color=TEXT_SECONDARY
            ),
            ft.Text(
                value=title, 
                size=24,
                weight=ft.FontWeight.W_600,
                color=TEXT_PRIMARY
            ),
            ft.Text(
                value=message,
                size=16,
                color=TEXT_SECONDARY,
                text_align=ft.TextAlign.CENTER,
                width=400
            )
        ]