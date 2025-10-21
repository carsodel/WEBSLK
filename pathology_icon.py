# new_project/components/pathology_icon.py
import reflex as rx
from new_project.styles.colors import Color, Text_color
from new_project.styles.styles import Size # Aún lo importamos por si lo usas en padding/border-radius

def pathology_icon(icon: str, text: str, href: str) -> rx.Component:
    # Mapea Size.SMALL.value a un valor de espaciado válido para VStack
    # Puedes ajustar este mapeo según cómo estén definidos tus "Size" y qué espaciado visual quieras
    # Por ejemplo, si Size.SMALL.value era '0.5em', podríamos mapearlo a '2' o '3'
    # del sistema de espaciado de Radix.
    # Para ser estrictos y si no quieres modificar Size.SMALL en styles.py:
    valid_spacing = "3" # Puedes elegir '1', '2', '3', '4', etc. entre '0' y '9'

    return rx.link(
        rx.vstack(
            rx.icon(
                tag=icon,
                size=30,  # Ya corregido a int
                color=Color.PRIMARY.value
            ),
            rx.text(
                text,
                text_align="center",
                color=Text_color.HEADER.value,
                font_weight="bold",
            ),
            spacing=valid_spacing, # <-- ¡CAMBIO AQUÍ! Usamos un string numérico
            align="center",
            width="100%",
            padding=Size.DEFAULT.value, # Estos deberían seguir siendo unidades CSS si Size.DEFAULT es así
            border_radius=Size.DEFAULT.value,
            _hover={
                "background_color": Color.SECONDARY.value,
                "cursor": "pointer",
            }
        ),
        href=href,
        is_external=False,
        text_decoration="none",
        _hover={
            "text_decoration": "none",
        }
    )