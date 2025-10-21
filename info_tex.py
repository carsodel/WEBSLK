import reflex as rx
from new_project.components.link_icon import link_icon
from new_project.components.link_icon import link_icon_2
from new_project.styles.styles import Size as Size
from new_project.styles.colors import Text_color as Text_color


def info(title:str,body:str) -> rx.Component: 
    return rx.flex(
        rx.text(
            title, 
            weight="bold", 
            color_scheme="blue"
        ),
        rx.text(
            f" {body}", size="3"
        ),
        color=Text_color.BODY.value,
        spacing="2"
    )