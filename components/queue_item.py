import flet as ft
from theme import BORDER, TEXT_PRIMARY, TEXT_SECONDARY
from datetime import datetime
import locale

try:
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
except locale.Error:
    locale.setlocale(locale.LC_TIME, 'Spanish_Spain.1252')

def get_platform_details(platform_name: str) -> dict:
    if platform_name and platform_name.lower() == "x":
        return {"icon": ft.Icons.CLOSE, "color": "#1DA1F2"}
    if platform_name and platform_name.lower() == "instagram":
        return {"icon": ft.Icons.CAMERA_ALT_OUTLINED, "color": "#E1306C"}
    
    return {"icon": ft.Icons.COMMENT, "color": TEXT_SECONDARY}


def format_datetime(iso_string):
    if not iso_string:
        return "Fecha no especificada"
    dt_object = datetime.fromisoformat(iso_string)
    return dt_object.strftime("Programado para el %d de %B, %H:%M")


class QueueItem(ft.Container):
    def __init__(self, post_data: dict, on_edit_click=None, on_delete_click=None):
        super().__init__()
        self.post_data = post_data
        self.on_edit_click = on_edit_click
        self.on_delete_click = on_delete_click
        print(f"[QueueItem] Creando item para post ID: {self.post_data.get('id')}")
        
        #Lógica de plataformas
        platform_name = self.post_data.get("platform", "default")
        platform_details = get_platform_details(platform_name)
        
        # Estilo del contenedor principal (la tarjeta)
        self.bgcolor = ft.Colors.with_opacity(0.03, ft.Colors.WHITE)
        self.border = ft.border.all(1, BORDER)
        self.border_radius = 8
        self.padding = 15
        
        #Logica de publicacion
        post_status = self.post_data.get("status", "scheduled")
        status_indicator = None
        
        if post_status == "published":
            status_indicator = ft.Row(
                spacing=5, 
                controls=[
                    ft.Icon(ft.Icons.CHECK_CIRCLE, color=ft.Colors.GREEN_500, size=14),
                    ft.Text("Publicado", color=ft.Colors.GREEN_500, size=14, weight=ft.FontWeight.BOLD)
                ]
            )
        
        elif post_status == "error":
            status_indicator = ft.Row(
                spacing=5,
                controls=[
                    ft.Icon(ft.Icons.ERROR_OUTLINE, color=ft.Colors.RED_500, size=14),
                    ft.Text("Error al publicar", color=ft.Colors.RED_500, size=14, weight=ft.FontWeight.BOLD)
                ]
            )
        else:
            status_indicator = ft.Text(
                value=format_datetime(self.post_data.get("scheduled_at")),
                color=TEXT_SECONDARY,
                size=12
            )
        
        # Contenido de la tarjeta
        
        self.delete_button = ft.IconButton(
            icon=ft.Icons.DELETE_OUTLINE,
            icon_size= 16,
            tooltip="Eliminar",
            data=self.post_data.get('id'),
            on_click=self.on_delete_click
        )
        
        self.edit_button = ft.IconButton(
            icon=ft.Icons.EDIT_CALENDAR_OUTLINED,
            icon_size=16,
            tooltip="Editar",
            on_click=lambda e: self.on_edit_click(self.post_data if self.on_edit_click else None)
        )
        
        self.delete_button.disabled = (post_status in ["published", "error"])
        self.edit_button.disabled = (post_status in ["published", "error"])
        
        #Logica de la foto de perfil
        avatar_content = ft.Icon(ft.Icons.PERSON, color=TEXT_SECONDARY)
        
        account_details = self.post_data.get("account_details")
        if account_details and account_details.get("profile_image_url"):
            avatar_widget = ft.CircleAvatar(background_image_src = account_details.get("profile_image_url"), radius=15)
        else:
            avatar_widget = ft.CircleAvatar(content=avatar_content, radius=15)
        
        self.content = ft.Column(
            spacing=10,
            controls=[
                # Fila superior: Icono de plataforma y Avatar
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Icon(
                            name=platform_details["icon"],
                            color=platform_details["color"],
                            size=20
                            ), # Icono de X/Twitter
                        avatar_widget
                    ]
                ),
                # Contenido del Post
                ft.Text(
                    value=self.post_data.get("content", "Contenido no disponible."),
                    color=TEXT_PRIMARY,
                    size=14
                ),
                ft.Divider(height=1, color=BORDER),
                # Fila inferior: Fecha programada y botones de acción
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        status_indicator,
                        ft.Row(
                            controls=[
                                self.edit_button,
                                self.delete_button
                            ]
                        )
                    ]
                )
            ]
        )