import flet as ft
#Paleta de colores
BACKGROUND = "#0D1117" 
SURFACE = "#161B22"    
PRIMARY = "#2F81F7"     
ON_PRIMARY = "#FFFFFF"  
TEXT_PRIMARY = "#E6EDF3" 
TEXT_SECONDARY = "#848D97" 
BORDER = "#30363D"     

#Tipografia

HEADING_FONT = "Roboto"
BODY_FONT = "Roboto"

APP_THEME= ft.Theme(
    color_scheme=ft.ColorScheme(
        primary=PRIMARY,
        on_primary=ON_PRIMARY,
        primary_container=SURFACE
    ),
    font_family=BODY_FONT
)