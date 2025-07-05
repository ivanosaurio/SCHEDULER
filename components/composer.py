# components/composer.py

import flet as ft
import threading, uuid, asyncio
from datetime import datetime
from theme import SURFACE, BORDER, PRIMARY, ON_PRIMARY, TEXT_SECONDARY, TEXT_PRIMARY
from components.thread_input import TweetInputControl
from services import supabase_service

EMOJI_LIST = [
    "😀", "😂", "😍", "🤔", "😎", "😭", "🙏", "❤️", "👍", "👎",
    "🔥", "🚀", "🎉", "💡", "💻", "✅", "✨", "👋", "💰", "📈",
]

class PostComposer(ft.Container):
    def __init__(self, on_schedule_click, on_thread_schedule_click, profile_image_url: str=None):
        super().__init__()
        
        # --- 1. CONFIGURACIÓN INICIAL Y GESTIÓN DE ESTADO ---
        self.on_schedule_click = on_schedule_click 
        self.on_thread_schedule_click = on_thread_schedule_click
        self.profile_image_url = profile_image_url
        self.uploaded_image_url = None
        self.selected_date = None
        self.selected_time = None
        
        self.is_thread_mode = False
        self.thread_controls = []

        # --- 2. DISEÑO Y COMPONENTES REUTILIZABLES ---
        self.bgcolor = SURFACE
        self.border = ft.border.all(1, BORDER)
        self.border_radius = 8 
        self.padding = 20
        
        self.file_picker = ft.FilePicker(on_result=self.handle_file_pick_result)
        self.date_picker = ft.DatePicker(
            on_change=self.handle_date_change, first_date=datetime.now(), help_text="Selecciona una fecha"
        )
        self.time_picker = ft.TimePicker(
            on_change=self.handle_time_change, confirm_text="Confirmar", help_text="Selecciona una hora"
        )

        # --- 3. CREACIÓN DE CONTROLES PARA CADA ESTADO ---
        self.avatar = ft.CircleAvatar(
            # ▼▼▼ CORRECCIÓN 1: USAR background_image_src ▼▼▼
            background_image_src=self.profile_image_url,
            content=ft.Icon(ft.Icons.PERSON, color=TEXT_SECONDARY),
            radius=20
        )
        self.single_tweet_textfield = ft.TextField(
            multiline=True,
            min_lines=3,
            border=ft.InputBorder.NONE,
            hint_text="¿Qué tienes en mente?",
            hint_style=ft.TextStyle(color=TEXT_SECONDARY),
            text_style=ft.TextStyle(color=TEXT_PRIMARY),
            expand=True,
            on_change=self._update_single_char_count
        )
        self.thread_inputs_container = ft.Column(spacing=0)

        self.image_preview = ft.Row(
            visible=False,
            controls=[
                ft.Icon(ft.Icons.IMAGE, color=TEXT_SECONDARY),
                ft.Text("Imagen adjunta.", color=TEXT_SECONDARY, style=ft.TextThemeStyle.BODY_SMALL),
                ft.IconButton(
                    icon=ft.Icons.CLOSE, 
                    icon_size=16, 
                    on_click=self.remove_image,
                    tooltip="Quitar imagen"
                )
            ]
        )
        # --- 4. ÁREA DE CONTENIDO DINÁMICO ---
        self.composer_content_area = ft.Column(
            controls=[
                ft.Row(
                    vertical_alignment=ft.CrossAxisAlignment.START,
                    spacing=15,
                    controls=[
                        self.avatar,
                        self.single_tweet_textfield
                        ]),
                self.image_preview
            ]
        )

        # --- 5. BOTONES Y CONTROLES DE LA BARRA INFERIOR ---
        self.feedback_message = ft.Text(value="", color=ft.Colors.GREEN_700, visible=False)
        self.scheduled_display = ft.Text("", color=TEXT_SECONDARY, visible=False)
        self.total_tweets_counter = ft.Text("", color=TEXT_SECONDARY, visible=False)
        self.main_char_counter = ft.Text("0/280", color=TEXT_SECONDARY, visible=True)
        
        self.image_button = ft.IconButton(
            icon=ft.Icons.IMAGE_OUTLINED, 
            tooltip="Añadir imagen",
            on_click=lambda _: self.file_picker.pick_files(
                allow_multiple=False,
                allowed_extensions=["png", "jpg", "jpeg"]
            )
        )
        self.emoji_button = ft.IconButton(
            icon=ft.Icons.EMOJI_EMOTIONS_OUTLINED, 
            tooltip="Añadir emoji",
            on_click=self.open_emoji_picker
        )
        self.add_tweet_button = ft.IconButton(
            icon=ft.Icons.ADD_CIRCLE_OUTLINE, tooltip="Convertir en hilo", on_click=self.add_tweet_input
        )
        self.add_another_tweet_button = ft.TextButton(
            "Añadir otro tweet",
            icon=ft.Icons.ADD,
            on_click=self.add_tweet_input,
            visible=False # Inicialmente oculto
        )
        self.schedule_button = ft.FilledButton(
            text="Programar", icon=ft.Icons.SEND, on_click=self.schedule_button_clicked,
            style=ft.ButtonStyle(bgcolor=PRIMARY, color=ON_PRIMARY)
        )
        
        # --- 6. ENSAMBLAJE FINAL ---
        self.content = ft.Column(
            spacing=15,
            controls=[
                self.composer_content_area,
                ft.Divider(height=1, color=BORDER),
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Row(
                            spacing=0,
                            controls=[
                                self.image_button,
                                self.emoji_button,
                                ft.IconButton(icon=ft.Icons.CALENDAR_MONTH_OUTLINED, on_click=lambda _: self.page.open(self.date_picker), tooltip="Programar fecha y hora"),
                                self.add_tweet_button
                            ]
                        ),
                        self.add_another_tweet_button,
                        ft.Row(
                            spacing=10,
                            controls=[
                                self.scheduled_display,
                                self.main_char_counter,
                                self.total_tweets_counter,
                                self.schedule_button]
                        )
                    ]
                ),
                ft.Row(controls=[self.feedback_message])
            ]
        )

    def initialize_composer(self):
        print("[Composer] Inicializando el estado del compositor.")
        self.clear()

    def update_avatar(self, profile_image_url: str | None):
        print(f"[Composer] Actualizando avatar con URL: {profile_image_url}")
        self.profile_image_url = profile_image_url
        if profile_image_url:
            # ▼▼▼ CORRECCIÓN 1.2: USAR background_image_src TAMBIÉN AQUÍ ▼▼▼
            self.avatar.background_image_src = profile_image_url
            self.avatar.content = None
        else:
            self.avatar.background_image_src = None
            self.avatar.content = ft.Icon(ft.Icons.PERSON, color=TEXT_SECONDARY)
        if self.is_thread_mode:
            for control in self.thread_controls:
                control.profile_image_url = profile_image_url
                control.controls[0].controls[0] = control.build_numerical_bubble()
        if self.page:
            self.update()

    def add_tweet_input(self, e=None):
        if not self.is_thread_mode:
            self.is_thread_mode = True
            first_tweet_content = self.single_tweet_textfield.value
            
            self.composer_content_area.controls.clear()
            self.composer_content_area.controls.append(self.thread_inputs_container)
            
            self.main_char_counter.visible = False
            self.total_tweets_counter.visible = True
            
            self.add_tweet_button.visible = False
            self.add_another_tweet_button.visible = True
            self.image_button.disabled = True
            self.emoji_button.disabled = True
            self.image_preview.visible = False
            
            self._create_new_thread_input_control(first_tweet_content)
            self._create_new_thread_input_control()
        else:
            self._create_new_thread_input_control()
        
        self.update_main_counter()
        if self.page:
            self.update()

    def _create_new_thread_input_control(self, content=""):
        """Función helper interna para crear y añadir un TweetInputControl."""
        new_tweet_number = len(self.thread_controls) + 1
        new_input = TweetInputControl(
            tweet_number=new_tweet_number,
            profile_image_url=self.profile_image_url,
            initial_content=content,
            on_delete=self.remove_tweet_input,
            on_text_change=self.update_main_counter
        )
        self.thread_controls.append(new_input)
        self.thread_inputs_container.controls.append(new_input)

    def remove_tweet_input(self, control_to_delete: TweetInputControl):
        if len(self.thread_controls) <= 1:
            return

        self.thread_controls.remove(control_to_delete)
        self.thread_inputs_container.controls.remove(control_to_delete)

        if len(self.thread_controls) == 1:
            self.is_thread_mode = False
            last_content = self.thread_controls[0].text_field.value
            self.clear() # La función clear se encarga de todo
            self.single_tweet_textfield.value = last_content # Restauramos el texto
        else:
            for i, control in enumerate(self.thread_controls):
                control.tweet_number = i + 1
                control.controls[0].controls[0] = control.build_numerical_bubble()
        
        self.update_main_counter()
        if self.page:
            self.update()
    
    def _update_single_char_count(self, e):
        """Actualiza el contador de caracteres para el modo de tweet único."""
        count = len(self.single_tweet_textfield.value)
        self.main_char_counter.value = f"{count}/280"
        if count > 280:
            self.main_char_counter.color = ft.Colors.RED_500
        else:
            self.main_char_counter.color = TEXT_SECONDARY
        
        if self.page:
            self.main_char_counter.update()
    
    def update_main_counter(self):
        if self.is_thread_mode:
            count= len(self.thread_controls)
            plural = "s" if count > 1 else ""
            self.total_tweets_counter.value = f"{count} Tweet{plural}"
            self.total_tweets_counter.visible = True
        else:
            self.total_tweets_counter.visible = False
        
        if self.page and self.total_tweets_counter.page:
            self.total_tweets_counter.update()
    
    def clear(self):
        """Reinicia el compositor a su estado inicial de 'Tweet Único'."""
        self.is_thread_mode = False
        self.selected_date = None
        self.selected_time = None
        self.uploaded_image_url = None
        self.thread_controls.clear()
        
        self.single_tweet_textfield.value = ""
        self.thread_inputs_container.controls.clear()
        self.composer_content_area.controls.clear()
        self.composer_content_area.controls.append(
            ft.Row(vertical_alignment=ft.CrossAxisAlignment.START, spacing=15, controls=[self.avatar, self.single_tweet_textfield])
        )
        self.composer_content_area.controls.append(self.image_preview)
        
        self.scheduled_display.visible = False
        
        self.main_char_counter.visible = True
        self.main_char_counter.value = "0/280"
        self.main_char_counter.color = TEXT_SECONDARY
        self.total_tweets_counter.visible = False
        
        self.add_tweet_button.visible = True
        self.add_another_tweet_button.visible = False
        self.image_button.disabled = False
        self.emoji_button.disabled = False
        self.image_preview.visible = False
        
        print("[Composer] Compositor reiniciado al estado de tweet único.")
        if self.page:
            self.update()
    
    async def handle_file_pick_result(self, e: ft.FilePickerResultEvent):
        """Manejador para cuando el usuario selecciona un archivo. Por ahora, solo muestra un mensaje."""
        if e.files:
            selected_file = e.files[0]
            unique_filename = f"{uuid.uuid4()}_{selected_file.name}"
            
            loop = asyncio.get_running_loop()
            result = await loop.run_in_executor(
                None,
                supabase_service.upload_image,
                selected_file.path,
                unique_filename
            )
            if result.get("success"):
                self.uploaded_image_url = result.get("url")
                self.show_feedback("Imagen subida con éxito.")
                self.image_preview.visible = True
                self.update()
            else:
                self.show_feedback(f"Error al subir imagen: {result.get('error')}", is_error=True)
        else:
            self.show_feedback("No se seleccionó ningún archivo.", is_error=True)
    
    def remove_image(self, e):
        self.uploaded_image_url = None
        self.image_preview.visible = False
        self.show_feedback("Imagen quitada.")
        self.update()
    
    def open_emoji_picker(self, e):
        def handle_emoji_click(e_emoji):
            self.single_tweet_textfield.value += e_emoji.control.text
            self.page.close(dlg)
            self.single_tweet_textfield.update()
            self._update_single_char_count(self.single_tweet_textfield)
        
        emoji_grid = ft.GridView(
            expand=True,
            runs_count=5,
            max_extent=40,
            spacing=5,
            run_spacing=5,
            child_aspect_ratio=1.0,
            controls=[
                ft.TextButton(
                    text=emoji,
                    on_click=handle_emoji_click,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8)))
                for emoji in EMOJI_LIST
            ]
        )
        
        dlg = ft.AlertDialog(
            modal=True,
            title=ft.Text("Selecciona un Emoji"),
            content=ft.Container(content=emoji_grid, width=300, height=200),
            actions=[ft.TextButton("Cerrar", on_click=lambda _: self.page.close(dlg))],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        self.page.open(dlg)
        self.page.update()
    
    def schedule_button_clicked(self, e):
        if self.selected_date and self.selected_time:
            final_datetime = datetime.combine(self.selected_date, self.selected_time)
        else:
            final_datetime = datetime.now()
        
        # ▼▼▼ CORRECCIÓN 4: LÓGICA DE PUBLICACIÓN CORRECTA ▼▼▼
        if self.is_thread_mode:
            posts_content = [
                control.text_field.value for control in self.thread_controls if control.text_field.value.strip()
            ]
            if not posts_content:
                self.show_feedback("El contenido del hilo no puede estar vacío.", is_error=True)
                return
            self.on_thread_schedule_click(final_datetime, posts_content)
        else:
            # Modo de tweet único
            content = self.single_tweet_textfield.value
            if not content.strip():
                self.show_feedback("El contenido no puede estar vacío.", is_error=True)
                return
            self.on_schedule_click(content, final_datetime, self.uploaded_image_url)

    # El resto de los métodos (handle_date_change, handle_time_change, show_feedback, etc.) no necesitan cambios
    def handle_date_change(self, e):
        self.selected_date = e.control.value
        self.page.open(self.time_picker)
    
    def handle_time_change(self,e):
        self.selected_time = e.control.value
        final_datetime = datetime.combine(self.selected_date, self.selected_time)
        self.scheduled_display.value = f"Programado para: {final_datetime.strftime('%d de %B, %H:%M')}"
        self.scheduled_display.visible = True
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
        if self.page and self.feedback_message.page:
            self.feedback_message.update()
            
    # Métodos que no se están usando y que generaban confusión. Los eliminamos para mayor claridad.
    # async def handle_file_pick_result(...):
    # def remove_image(...):
    # def open_emoji_picker(...):
    # def update_char_count(...):