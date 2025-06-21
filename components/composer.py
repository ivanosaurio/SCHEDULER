import flet as ft
import threading, uuid
from services.supabase_service import upload_image
from datetime import datetime, time
from theme import SURFACE, BORDER, PRIMARY, ON_PRIMARY, TEXT_SECONDARY, TEXT_PRIMARY

class PostComposer(ft.Container):
    def __init__(self, on_schedule_click):
        super().__init__()
        
        self.on_schedule_click = on_schedule_click 
        self.uploaded_image_url = None
        
        self.selected_date = None
        self.selected_time = None
        #Diseno del container
        self.bgcolor = SURFACE
        self.border = ft.border.all(1, BORDER)
        self.border_radius = 8 
        self.padding = 20
        
        self.file_picker = ft.FilePicker(on_result=self.handle_file_pick_result)
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
        
        self.image_indicator = ft.Row(
            visible=False,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Icon(ft.Icons.CHECK_CIRCLE, color=ft.Colors.GREEN_500),
                ft.Text("Imagen Adjunta", size=12, color=TEXT_SECONDARY),
                ft.IconButton(
                    icon=ft.Icons.CLOSE,
                    icon_size=16, 
                    on_click=self.remove_image,
                    tooltip="Quitar imagen"
                )
            ]
        )
        
        self.schedule_button = ft.FilledButton(
            text="Programar",
            icon=ft.Icons.SEND,
            on_click=self.schedule_button_clicked,
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
                                ft.IconButton(
                                    icon=ft.Icons.IMAGE_OUTLINED,
                                    tooltip="Añadir imagen",
                                    icon_color=TEXT_SECONDARY,
                                    on_click=lambda _: self.file_picker.pick_files(allow_multiple=False, allowed_extensions=["png", "jpg", "jpeg", "gift"])
                                    ),
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
                self.image_indicator,
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
    
    async def handle_file_pick_result(self, e: ft.FilePickerResultEvent):
        if e.files:
            self.show_feedback("Subiendo imagen...", is_error=False)
            
            selected_file = e.files[0]
            
            unique_filename = f"{uuid.uuid4()}_{selected_file.name}"
            
            result = upload_image(file_path=selected_file.path, file_name=unique_filename)
            
            if result.get("success"):
                self.uploaded_image_url = result.get("url")
                self.show_feedback("Imagen subida con éxito.")
                self.image_indicator.visible =True
                self.update()
            else:
                self.show_feedback(f"Error: {result.get('error')}", is_error=True)
        else:
            self.show_feedback("No se seleccionó ningún archivo.", is_error=True)
    
    def remove_image(self, e):
        self.uploaded_image_url = None
        self.image_indicator.visible = False
        self.show_feedback("Imagen quitada")
        self.update()
    
    async def schedule_button_clicked(self, e):
        final_datetime = None
        if self.selected_date and self.selected_time:
            final_datetime = datetime.combine(self.selected_date, self.selected_time)
        
        self.on_schedule_click(
            self.text_field.value,
            final_datetime,
            self.uploaded_image_url
            )
    
    def handle_date_change(self, e):
        self.selected_date = e.control.value
        print(f"Fecha seleccionada: {self.selected_date}")
        
        self.page.open(self.time_picker)
    
    def handle_time_change(self,e):
        self.selected_time = e.control.value
        print(f"Hora seleccionada: {self.selected_time}")
        
        final_datetime = datetime.combine(self.selected_date, self.selected_time)
        
        self.scheduled_display.value = f"Programado para: {final_datetime.strftime('%d de %B, %H:%M')}"
        self.scheduled_display.visible = True
        self.update()
    
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
        self.selected_date = None
        self.selected_time = None
        self.scheduled_display.visible = False
        self.remove_image(None)
        self.update_char_count(None)
        self.feedback_message.visible = False 
        self.feedback_message.update()
        self.text_field.update()
        self.update()
    
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