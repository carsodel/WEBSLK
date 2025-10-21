import reflex as rx
from new_project.styles.styles import Size as Size
from new_project.styles.colors import Text_color as Text_color


import datetime

def footer() -> rx.Component: 
    return rx.flex(

        rx.text(f"""{datetime.date.today().year} SoloKiamix® by Carlos Soler & Laura Lorente""", 
            size="1",
            color=Text_color.FOOTER.value
            ),
        margin_bottom=Size.BIG.value,
        margin_top="0px !important",
        direction="column",
        spacing="3",
    )