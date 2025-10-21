import reflex as rx
from new_project.styles.styles import Size as Size
from new_project.styles.colors import Color as Color
from new_project.styles.colors import Text_color as Text_color
import new_project.styles.styles as styles

def navbar() -> rx.Component:
    return rx.hstack(
        rx.flex(
            rx.text(
                "Solo",
                color=Color.SECONDARY.value,
            ),
            rx.text(
                "Kia",
                color=Color.PRIMARY.value,
            ),
            rx.text(
                "Mix",
                color=Color.SECONDARY.value
            ),
            rx.spacer(),
            rx.text(
                "S",
                color=Color.SECONDARY.value
            ),
            rx.text(
                "K",
                color=Color.PRIMARY.value
            ),
            rx.text(
                "M",
                color=Color.SECONDARY.value
            ),
            width="100%",
            style=styles.nav_bar_style
        ),
        position = "sticky",
        bg = Color.CONTENT.value,
        padding_x= Size.BIG.value,
        padding_y= Size.DEFAULT.value,
        z_index="999",
        top="0"
    )