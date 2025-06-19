import flet as ft
import threading
from datetime import datetime, time
from theme import SURFACE, BORDER, PRIMARY, ON_PRIMARY, TEXT_SECONDARY, TEXT_PRIMARY

class PostComposer(ft.Container):
    def __init__(self, on_schedule_click):
        super().__init__()
        
        self.on_schedule_click = on_schedule_click 
        
        #Hora
        self.selected_date = None
        self.selected_time  = None
        #Diseno del container
        self.bgcolor = SURFACE
        self.border = ft.border.all(1, BORDER)
        self.border_radius = 8 
        self.padding = 20
        
        self.char_counter = ft.Text("0/280", color=TEXT_SECONDARY)
        
        self.feedback_message = ft.Text(value="", color=ft.Colors.GREEN_700, visible=False)
        
        #Elementos UI
        
        self.date_picker = ft.DatePicker(
            on_change=self.handle_date_change,
            on_dismiss=lambda e: print("DatePicker cerrado"),
            first_date=datetime.now(),
            help_text="Selecciona una fecha para tu post"
        )
        
        self.time_picker = ft.TimePicker(
            on_change=self.handle_time_change,
            on_dismiss=lambda e: print("TimePicker cerrado"),
            confirm_text="Confirmar",
            help_text="Selecciona una hora"
        )
        
        self.scheduled_display = ft.Text(
            "",
            color=TEXT_SECONDARY,
            visible=False
        )
        
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
                self.date_picker,
                self.time_picker,
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
                                ft.IconButton(icon=ft.Icons.EMOJI_EMOTIONS_OUTLINED, tooltip="Añadir emoji", icon_color=TEXT_SECONDARY),
                                ft.IconButton(
                                    icon=ft.Icons.CALENDAR_MONTH_OUTLINED,
                                    tooltip="Programar fecha y hora",
                                    icon_color=TEXT_SECONDARY,
                                    on_click=lambda e: self.page.open(self.date_picker)
                                    )
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
                        self.scheduled_display 
                        ]
                    ),
                ft.Row(
                    controls=[
                        self.feedback_message
                    ]
                )
            ]
        )
    
    async def handle_date_change(self, e):
        self.selected_date = e.control.value
        print(f"Fecha seleccionada: {self.selected_date}")
        
        await self.page.open(self.time_picker)
    
    async def handle_time_change(self,e):
        self.selected_time = e.control.value
        print(f"Hora seleccionada: {self.selected_time}")
        
        final_datetime = datetime.combine(self.selected_date, self.selected_time)
        
        self.scheduled_display.value = f"Programado para: {final_datetime.strftime('%d de %B, %H:%M')}"
        self.scheduled_display.visible = True
        await self.update()
    
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