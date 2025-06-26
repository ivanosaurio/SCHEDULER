import flet as ft
import threading, uuid, asyncio
from services import supabase_service
from datetime import datetime, time
from theme import SURFACE, BORDER, PRIMARY, ON_PRIMARY, TEXT_SECONDARY, TEXT_PRIMARY

EMOJI_LIST = [
    "😀", "😂", "😍", "🤔", "😎", "😭", "🙏", "❤️", "👍", "👎",
    "🔥", "🚀", "🎉", "💡", "💻", "✅", "✨", "👋", "💰", "📈",
]

class PostComposer(ft.Container):
    def __init__(self, on_schedule_click, on_thread_schedule_click, profile_image_url: str=None):
        super().__init__()
        
        self.on_schedule_click = on_schedule_click 
        self.on_thread_schedule_click = on_thread_schedule_click
        self.uploaded_image_url = None
        self.selected_date = None
        self.selected_time = None
        
        #Hilo
        self.is_thread_mode = False
        self.thread_inputs_container = ft.Column(spacing=10)
        self.thread_text_fields = []
        
        #Diseno del container
        self.bgcolor = SURFACE
        self.border = ft.border.all(1, BORDER)
        self.border_radius = 8 
        self.padding = 20
        
        self.file_picker = ft.FilePicker(on_result=self.handle_file_pick_result)
        self.char_counter = ft.Text("0/280", color=TEXT_SECONDARY)
        
        self.feedback_message = ft.Text(value="", color=ft.Colors.GREEN_700, visible=False)
        
        #Elementos UI
        
        self.avatar = ft.CircleAvatar(
            content=ft.Icon(ft.Icons.PERSON, color=TEXT_SECONDARY)
        )
        
        if profile_image_url:
            self.avatar.foreground_image_src = profile_image_url
            self.avatar.content = None
        
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
        
        self.single_tweet_textfield = ft.TextField(
            multiline=True,
            min_lines=4,
            border=ft.InputBorder.NONE,
            hint_text="¿Qué tienes en mente?",
            hint_style=ft.TextStyle(color=TEXT_SECONDARY),
            text_style=ft.TextStyle(color=TEXT_PRIMARY, font_family="Roboto"),
            expand=True,
            on_change=lambda e: self.update_main_char_counter()
        )
        
        self.composer_content_area = ft.Column(
            controls=[
                ft.Row(
                    vertical_alignment=ft.CrossAxisAlignment.START,
                    controls=[
                        self.avatar,
                        self.single_tweet_textfield
                    ]
                )
            ]
        )
        
        self.add_to_thread_button = ft.IconButton(
            icon=ft.Icons.ADD_CIRCLE_OUTLINE_ROUNDED,
            tooltip="Añadir Tweet al Hilo",
            on_click=self.add_tweet_to_thread,
            icon_color=TEXT_SECONDARY
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
                self.composer_content_area,
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Row(
                            controls=[
                                ft.IconButton(
                                    icon=ft.Icons.IMAGE_OUTLINED,
                                    tooltip="Añadir imagen",
                                    icon_color=TEXT_SECONDARY,
                                    on_click=lambda _:self.file_picker.pick_files(allow_multiple=False, allowed_extensions=["png", "jpg", "jpeg", "gif"])
                                ),
                                ft.IconButton(
                                    icon=ft.Icons.EMOJI_EMOTIONS_OUTLINED,
                                    tooltip="Añadir emoji",
                                    icon_color=TEXT_SECONDARY,
                                    on_click=self.open_emoji_picker
                                ),
                                ft.IconButton(
                                    icon=ft.Icons.CALENDAR_MONTH_OUTLINED,
                                    tooltip="Añadir emoji",
                                    icon_color=TEXT_SECONDARY,
                                    on_click=lambda e: self.page.open(self.date_picker)
                                ),
                                self.add_to_thread_button
                            ]
                        ),
                        ft.Row(
                            controls=[
                                self.char_counter,
                                ft.Container(width=10),
                                self.schedule_button
                            ]
                        ),
                        self.image_indicator,
                        ft.Row(controls=[self.scheduled_display]),
                        ft.Row(controls=[self.feedback_message])
                    ]
                )
            ]
        )
    
    def create_thread_tweet_input(self, content=""):
        char_counter = ft.Text("0/280", color=TEXT_SECONDARY, size=12)
        text_field = ft.TextField(
            value=content,
            multiline=True,
            min_lines=2,
            border=ft.InputBorder.UNDERLINE,
            hint_text="Añade otro tweet...",
            hint_style=ft.TextStyle(color=TEXT_SECONDARY),
            text_style=ft.TextStyle(color=TEXT_PRIMARY),
            on_change=lambda e: self.update_char_count(e.control.value, char_counter),
            expand=True
        )
        
        self.thread_text_fields.append(text_field)
        
        input_row = ft.Row(
            vertical_alignment=ft.CrossAxisAlignment.START,
            controls=[
                ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    width=40,
                    controls=[
                        ft.Icon(ft.Icons.MORE_VERT, color=BORDER)
                    ]
                ),
                ft.Column(
                    expand=True,
                    controls=[
                        text_field,
                        ft.Row([char_counter], alignment=ft.MainAxisAlignment.END)
                    ]
                ),
                ft.IconButton(
                    icon=ft.Icons.REMOVE_CIRCLE_OUTLINE,
                    on_click=lambda e: self.remove_tweet_from_thread(input_row),
                    icon_color=TEXT_SECONDARY,
                    tooltip="Eliminar Tweet"
                )
            ]
        )
        
        self.update_char_count(content, char_counter)
        return input_row
    
    def add_tweet_to_thread(self, e):
        if not self.is_thread_mode:
            self.is_thread_mode = True
            
            first_tweet_content = self.single_tweet_textfield.value
            
            self.composer_content_area.controls.clear()
            self.composer_content_area.controls.append(self.thread_inputs_container)
            self.thread_text_fields.clear()
            self.thread_inputs_container.controls.clear()
            
            self.thread_inputs_container.controls.append(self.create_thread_tweet_input(first_tweet_content))
            self.thread_inputs_container.controls.append(self.create_thread_tweet_input())
            self.update_main_char_counter()
        else:
            self.thread_inputs_container.controls.append(self.create_thread_tweet_input())
            self.update()
    
    def remove_tweet_from_thread(self, row_to_remove: ft.Row):
        textfield_to_remove = row_to_remove.controls[1].controls[0]
        if textfield_to_remove in self.thread_text_fields:
            self.thread_text_fields.remove(textfield_to_remove)
        
        self.thread_inputs_container.controls.remove(row_to_remove)
        
        if len(self.thread_text_fields) < 2:
            self.is_thread_mode = False
            last_content = self.thread_text_fields[0].value if self.thread_text_fields else ""
            self.composer_content_area.controls.clear()
            self.single_tweet_textfield.value = last_content
            self.composer_content_area.controls.append(
                ft.Row(
                    vertical_alignment=ft.CrossAxisAlignment.START,
                    controls=[self.avatar, self.single_tweet_textfield]
                )
            )
            self.thread_text_fields.clear()
        
        self.update_main_char_counter()
        self.update()
    
    def update_avatar(self, profile_image_url: str | None):
        print(f"[Composer] Actualizando avatar con URL: {profile_image_url}")
        if profile_image_url:
            self.avatar.foreground_image_src = profile_image_url
            self.avatar.content = None
        else:
            self.avatar.background_image_src = None
            self.avatar.content = ft.Icon(ft.Icons.PERSON, color=TEXT_SECONDARY)
        if self.page:
            print(f"[Composer] self.page existe. Intentando self.update() para redibujar todo el compositor.")
            self.update()
        else:
            print("[Composer] ADVERTENCIA: self.page es None. No se puede llamar a update().")
    
    async def handle_file_pick_result(self, e: ft.FilePickerResultEvent):
        if e.files:
            self.show_feedback("Subiendo imagen...", is_error=False)
            
            selected_file = e.files[0]
            
            unique_filename = f"{uuid.uuid4()}_{selected_file.name}"
            
            loop = asyncio.get_running_loop()
            result = await loop.run_in_executor(None, supabase_service.upload_image, selected_file.path, unique_filename)
            
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
    
    def schedule_button_clicked(self, e):
        final_datetime = None
        if self.selected_date and self.selected_time:
            final_datetime = datetime.combine(self.selected_date, self.selected_time)
        if self.is_thread_mode:
            posts_content = [tf.value for tf in self.thread_text_fields if tf.value.strip()]
            if len(posts_content) < 2:
                self.show_feedback("Error: Un hilo debe tener al menos dos tweets.", is_error=True)
                return
            print(f"Programando hilo con {len(posts_content)} tweets para las {final_datetime}")
            self.on_thread_schedule_click(final_datetime, posts_content)
        else:
            content = self.single_tweet_textfield.value
            if not content.strip():
                self.show_feedback("Error: El contenido no puede estar vacío.", is_error=True)
                return
            print(f"Programando post individual para las {final_datetime}")
            self.on_schedule_click(content, final_datetime, self.uploaded_image_url)
    
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
    
    def open_emoji_picker(self, e):
        def handle_emoji_click(e_emoji):
            target_field = self.thread_text_fields[-1] if self.is_thread_mode else self.single_tweet_textfield
            target_field.value += e_emoji.control.text
            self.page.close(dlg)
            target_field.update()
            
            if self.is_thread_mode:
                mini_composer_row = self.thread_inputs_container.controls[-1]
                char_counter = mini_composer_row.controls[1].controls[1].controls[0]
                self.update_char_count(target_field.value, char_counter)
            else:
                self.update_char_count(target_field.value, self.char_counter)
            target_field.update()
        
        emoji_grid = ft.GridView(
            expand=1,
            runs_count=5,
            max_extent=40,
            spacing=5,
            run_spacing=5,
            child_aspect_ratio=1.0
        )
        for emoji in EMOJI_LIST:
            emoji_grid.controls.append(
                ft.TextButton(
                    text=emoji,
                    on_click=handle_emoji_click,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=8)
                    )
                )
            )
        
        dlg = ft.AlertDialog(
            modal=True,
            title=ft.Text("Selecciona un Emoji"),
            content=ft.Container(
                content=emoji_grid,
                width=300,
                height=200
            ),
            actions_alignment=ft.MainAxisAlignment.END,
            actions=[
                ft.TextButton("Cerrar", on_click=lambda _: self.page.close(dlg))
            ]
        )
        
        self.page.open(dlg)
        self.page.update()
    
    def update_char_count(self, text_value: str, char_counter_control: ft.Text):
        count = len(text_value)
        char_counter_control.value = f"{count}/280"
        if count > 280:
            char_counter_control.color = ft.Colors.RED_500
        else:
            self.char_counter.color = TEXT_SECONDARY
        if char_counter_control.page:
            char_counter_control.update()
    
    def update_main_char_counter(self):
        if self.is_thread_mode:
            count = len(self.thread_text_fields)
            self.char_counter.value = f"{count} Tweets"
            self.char_counter.color = TEXT_SECONDARY
        else:
            self.update_char_count(self.single_tweet_textfield.value, self.char_counter)
        
        if self.char_counter.page:
            self.char_counter.update()
    
    def clear(self):
        self.is_thread_mode = False
        self.single_tweet_textfield.value = ""
        self.thread_text_fields.clear()
        self.thread_inputs_container.controls.clear()
        
        self.composer_content_area.controls.clear()
        self.composer_content_area.controls.append(
            ft.Row(
                vertical_alignment=ft.CrossAxisAlignment.START,
                controls=[self.avatar, self.single_tweet_textfield]
                )
        )
        
        self.selected_date = None
        self.selected_time = None
        self.scheduled_display.visible = False
        self.remove_image(None)
        
        self.update_main_char_counter()
        self.feedback_message.visible = False 
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