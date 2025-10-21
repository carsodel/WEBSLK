import reflex as rx
from new_project.components.link_icon import link_icon
from new_project.components.link_icon import link_icon_2
from new_project.styles.styles import Size as Size
from new_project.components.info_tex import info
from new_project.styles.colors import Text_color as Text_color
from new_project.styles.colors import Color as Color




def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                src="/logo_kiamix_2.png",
                fallback="Kiamix",
                size="8",
                color_scheme="cyan",
                variant="soft",
                bg=Color.CONTENT.value,
                padding="2px",
                border="6px",
                border_color=Color.PRIMARY.value,
                radius="large"
                ),
            rx.flex(
                rx.text(
                    "Solo",
                    size="9",
                    weight="light",
                    color="#708238"
                    ),
                rx.text(
                    "Kiamix",
                    size="9",
                    weight="bold",
                    align="right",
                    color="#bfa76f"
                    ),
                rx.text(
                    "Salud integral para tu vida",
                    margin_top="0px !important",
                    color=Text_color.BODY.value,
                    font_family="Confortaa-Medium"
                    ),
                direction="column",

            ),
            
        ),

        rx.flex(
            info("+10", "años de formación"),
            rx.spacer(),
            width="100%"

        ),
        spacing="8",
        align_items="start"
        
    )
