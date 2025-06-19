import flet as ft
import threading
from theme import SURFACE, BORDER, PRIMARY, ON_PRIMARY, TEXT_SECONDARY, TEXT_PRIMARY

class PostComposer(ft.Container):
    def __init__(self, on_schedule_click):
        super().__init__()
        
        self.on_schedule_click = on_schedule_click 
        self.bgcolor = SURFACE
        self.border = ft.border.all(1, BORDER)
        self.border_radius = 8 
        self.padding = 20
        
        self.char_counter = ft.Text("0/280", color=TEXT_SECONDARY)
        
        self.feedback_message = ft.Text(value="", color=ft.Colors.GREEN_700, visible=False)
        
        #Elementos UI
        self.text_field = ft.TextField(
            multiline=True,
            min_lines=4,
            border=ft.InputBorder.NONE,
            hint_text="¿Qué tienes en mente?",
            hint_style=ft.TextStyle(color=TEXT_SECONDARY),
            text_style=ft.TextStyle(color=TEXT_PRIMARY, font_family="Roboto"),
            expand=True,
            on_change=self.update_char_count
        )
        self.schedule_button = ft.FilledButton(
            text="Programar",
            icon=ft.Icons.SEND,
            on_click=lambda e: self.on_schedule_click(self.text_field.value),
            style=ft.ButtonStyle(
                bgcolor=PRIMARY,
                color=ON_PRIMARY
                )
            )
        
        self.content = ft.Column(
            spacing=15,
            controls=[
                ft.Row(
                    vertical_alignment=ft.CrossAxisAlignment.START,
                    controls=[
                        ft.CircleAvatar(content=ft.Icon(ft.Icons.PERSON, color=TEXT_SECONDARY)),
                        self.text_field
                    ]
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Row(
                            controls=[
                                ft.IconButton(icon=ft.Icons.IMAGE_OUTLINED, tooltip="Añadir imagen", icon_color=TEXT_SECONDARY),
                                ft.IconButton(icon=ft.Icons.EMOJI_EMOTIONS_OUTLINED, tooltip="Añadir emoji", icon_color=TEXT_SECONDARY)
                            ]
                        ),
                        ft.Row(
                            controls = [
                                self.char_counter,
                                ft.Container(width=10),
                                self.schedule_button
                                ]
                        )
                    ]
                ),
                ft.Row(
                    controls=[
                        self.feedback_message
                    ]
                )
            ]
        )
    
    def update_char_count(self,e):
        count = len(self.text_field.value)
        self.char_counter.value = f"{count}/280"
        if count > 280:
            self.char_counter.color = ft.Colors.RED_500
        else:
            self.char_counter.color = TEXT_SECONDARY
        self.char_counter.update()
    
    def clear(self):
        self.text_field.value = ""
        self.update_char_count(None)
        self.feedback_message.visible = False 
        self.feedback_message.update()
        self.text_field.update()
    
    def show_feedback(self, message: str, is_error :bool= False):
        self.feedback_message.value = message
        self.feedback_message.color = ft.Colors.RED_500 if is_error else ft.Colors.GREEN_700
        self.feedback_message.visible = True
        self.feedback_message.update()
        
        timer = threading.Timer(3.0, self.hide_feedback)
        timer.start()
    
    def hide_feedback(self):
        self.feedback_message.visible = False
        if self.page:
            self.feedback_message.update()