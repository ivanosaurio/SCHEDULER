import flet as ft
from theme import BORDER, TEXT_PRIMARY, TEXT_SECONDARY
from datetime import datetime
import locale

try:
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
except locale.Error:
    locale.setlocale(locale.LC_TIME, 'Spanish_Spain.1252')


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
        
        # Estilo del contenedor principal (la tarjeta)
        self.bgcolor = ft.Colors.with_opacity(0.03, ft.Colors.WHITE)
        self.border = ft.border.all(1, BORDER)
        self.border_radius = 8
        self.padding = 15

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
        
        self.content = ft.Column(
            spacing=10,
            controls=[
                # Fila superior: Icono de plataforma y Avatar
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Icon(ft.Icons.CLOSE, color="#1DA1F2", size=20), # Icono de X/Twitter
                        ft.CircleAvatar(content=ft.Icon(ft.Icons.PERSON, color=TEXT_SECONDARY), radius=15)
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
                        ft.Text(
                            value=format_datetime(self.post_data.get("scheduled_at")),
                            color=TEXT_SECONDARY,
                            size=12
                        ),
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