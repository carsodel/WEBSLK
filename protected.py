import reflex as rx
from ..ui.base import base_page
from rxconfig import config
import reflex_local_auth

#@rx.page(route="/about")
@reflex_local_auth.require_login
def protected_page() -> rx.Component:
    my_child =rx.vstack(
                rx.heading("Protected Page", size="9"),
                rx.text(
                    "Nuestra formación ",
                    rx.code(f"{config.app_name}/{config.app_name}.py"),
                    size="5",
                ),
                spacing="5",
                justify="center",
                min_height="85vh",
                text_align="center",
                align="center",

            ),
    return base_page(
        my_child
    ),