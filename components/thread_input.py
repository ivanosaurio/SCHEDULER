import flet as ft
from theme import BORDER, TEXT_SECONDARY, TEXT_PRIMARY, SURFACE

class TweetInputControl(ft.Row):
    def __init__(self, tweet_number: int, profile_image_url: str, on_delete, on_text_change):
        super().__init__()
        
        self.tweet_number = tweet_number
        self.profile_image_url = profile_image_url
        self.on_delete = on_delete
        self.on_text_change = on_text_change
        
        self.vertical_alignment = ft.CrossAxisAlignment.START
        self.spacing = 10
        
        #Components
        self.text_field = ft.TextField(
            multiline=True,
            min_lines=3,
            border=ft.InputBorder.NONE,
            hint_text="Añade otro tweet..." if tweet_number > 1 else "¿Qué tienes en mente?",
            hint_style=ft.TextStyle(color=TEXT_SECONDARY),
            text_style=ft.TextStyle(color=TEXT_PRIMARY),
            on_change=self.handle_text_change
        )
        
        self.char_counter = ft.Text("0/280", color=TEXT_SECONDARY, size=12)
        
        self.controls = [
            ft.Column(
                width=40,
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    self.build_numerical_bubble(),
                    ft.Container(
                        width=2,
                        height=100,
                        bgcolor=BORDER,
                        expand=True
                    )
                ]
            ),
            ft.Container(
                bgcolor=SURFACE,
                border=ft.border.all(1, BORDER),
                border_radius=8,
                padding=ft.padding.only(left=15, top=5, right=5, bottom=5),
                expand=True,
                content=ft.Column(
                    spacing=0,
                    controls=[
                        self.text_field,
                        ft.Row(
                            alignment=ft.MainAxisAlignment.END,
                            controls=[
                                self.char_counter,
                                ft.IconButton(
                                    icon=ft.Icons.REMOVE_CIRCLE_OUTLINE,
                                    on_click=lambda e: self.on_delete(self),
                                    icon_color=TEXT_SECONDARY,
                                    tooltip="Eliminar Tweet"
                                )
                            ]
                        )
                    ]
                )
            )
        ]
    
    def build_numerical_bubble(self):
        return ft.Stack(
            width=32,
            height=32,
            controls=[
                ft.CircleAvatar(
                    background_image_src=self.profile_image_url,
                    radius=16
                ),
                ft.Container(
                    alignment=ft.alignment.center,
                    border_radius=16,
                    bgcolor=ft.Colors.with_opacity(0.4, ft.Colors.BLACK),
                    content=ft.Text(
                        str(self.tweet_number),
                        size=14,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.WHITE
                    )
                )
            ]
        )
    
    def handle_text_change(self, e):
        count = len(e.control.value)
        self.char_counter.value = f"{count}/280"
        if count > 280:
            self.char_counter.color = ft.Colors.RED_500
        else:
            self.char_counter.color = TEXT_SECONDARY
        
        self.on_text_change()
        
        if self.page:
            self.update()