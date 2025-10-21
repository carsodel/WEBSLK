
import reflex as rx

from rxconfig import config

from .nav_bar import nav_bar


def base_page(child: rx.Component, *args, **kwargs) -> rx.Component:

    return rx.fragment(
        nav_bar(),
        rx.box( 
            child,
            #bg=rx.color("accent", 3),
            padding="1em",
            width="100%",
        ),
        rx.logo(),
        rx.color_mode.button(position="bottom-left"),
    )