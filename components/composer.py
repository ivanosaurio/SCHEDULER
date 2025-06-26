import flet as ft
import threading, uuid, asyncio
from services import supabase_service
from datetime import datetime, time
from theme import SURFACE, BORDER, PRIMARY, ON_PRIMARY, TEXT_SECONDARY, TEXT_PRIMARY
from components.thread_input import TweetInputControl

EMOJI_LIST = [
    "😀", "😂", "😍", "🤔", "😎", "😭", "🙏", "❤️", "👍", "👎",
    "🔥", "🚀", "🎉", "💡", "💻", "✅", "✨", "👋", "💰", "📈",
]

class PostComposer(ft.Container):
    def __init__(self, on_schedule_click, on_thread_schedule_click, profile_image_url: str=None):
        super().__init__()
        
        self.on_schedule_click = on_schedule_click 
        self.on_thread_schedule_click = on_thread_schedule_click
        self.profile_image_url = profile_image_url
        self.uploaded_image_url = None
        self.selected_date = None
        self.selected_time = None
        
        #Hilo
        self.thread_controls = []
        
        #Diseno del container
        self.bgcolor = SURFACE
        self.border = ft.border.all(1, BORDER)
        self.border_radius = 8 
        self.padding = 20
        
        self.file_picker = ft.FilePicker(on_result=self.handle_file_pick_result)
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
        
        self.thread_inputs_container = ft.Column(spacing=0)
        
        #Feeback y Fecha programada
        self.scheduled_display = ft.Text(
            "",
            color=TEXT_SECONDARY,
            visible=False
        )
        self.feedback_message = ft.Text(value="", color=ft.Colors.GREEN_700, visible=False)
        
        #Nuevos tweets
        self.add_tweet_button = ft.TextButton(
            text="Añadir otro tweet...",
            icon=ft.Icons.ADD,
            on_click=self.add_tweet_input
        )
        
        self.total_tweets_counter = ft.Text("1 Tweet", color=TEXT_SECONDARY)
        
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
                self.thread_inputs_container,
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        self.add_tweet_button
                    ]
                ),
                ft.Divider(height=1, color=BORDER),
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        self.scheduled_display,
                        ft.Row(
                            spacing=10,
                            controls=[
                                ft.IconButton(
                                    icon=ft.Icons.CALENDAR_MONTH_OUTLINED,
                                    on_click=lambda _: self.page.open(self.date_picker),
                                    tooltip="Programar fecha y hora"
                                ),
                                self.total_tweets_counter,
                                self.schedule_button
                            ]
                        )
                    ]
                ),
                ft.Row(controls=[self.feedback_message])
            ]
        )
    
    def initialize_composer(self):
        print("[Composer] Inicializando el estado del compositor.")
        if not self.thread_inputs_container.controls:
            self.add_tweet_input()
    
    def add_tweet_input(self, e=None):
        new_tweet_number = len(self.thread_controls) + 1
        new_input = TweetInputControl(
            tweet_number=new_tweet_number,
            profile_image_url=self.profile_image_url,
            on_delete=self.remove_tweet_input,
            on_text_change=self.update_main_char_counter
        )
        
        self.thread_controls.append(new_input)
        self.thread_inputs_container.controls.append(new_input)
        self.update_main_counter()
        if self.page:
            self.update()
    
    def remove_tweet_input(self, control_to_delete: TweetInputControl):
        if len(self.thread_controls) <=1:
            self.show_feedback("No puedes eliminar el único tweet.", is_error=True)
            return
        
        self.thread_controls.remove(control_to_delete)
        self.thread_inputs_container.controls.remove(control_to_delete)
        
        for i, control in enumerate(self.thread_controls):
            control.tweet_number = i + 1
            control.controls[0].controls[0] = control.build_numerical_bubble()
        
        self.update_main_counter()
        if self.page:
            self.update()
    
    def update_main_counter(self):
        count = len(self.thread_controls)
        plural = "s" if count > 1 else ""
        self.total_tweets_counter.value = f"{count} Tweet{plural}"
        
        if self.total_tweets_counter.page:
            self.total_tweets_counter.update()
    
    
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
        if not self.selected_date or not self.selected_time:
            self.show_feedback("Debes seleccionar una fecha y hora para programar.", is_error=True)
            return
        final_datetime = datetime.combine(self.selected_date, self.selected_time)
        
        posts_content = [
            control.text_field.value for control in self.thread_controls if control.text_field.value.strip()
        ]
        
        if not posts_content:
            self.show_feedback("El contenido no puede estar vacío.", is_error=True)
            return
        
        if len(posts_content) == 1:
            self.on_schedule_click(posts_content[0], final_datetime, self.uploaded_image_url)
        else:
            self.on_thread_schedule_click(final_datetime, posts_content)
    
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
        self.thread_controls.clear()
        self.thread_inputs_container.controls.clear()
        
        self.selected_date = None
        self.selected_time = None
        
        self.add_tweet_input()
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