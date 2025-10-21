import reflex as rx
import new_project.styles.styles as styles


def link_icon(url:str) -> rx.Component: 
    return rx.link(
        rx.icon(
            tag="baby"
        ),
        href=url,
        is_external=True,
    )


def link_icon_2(url:str) -> rx.Component: 
    return rx.link(
        rx.icon(
            tag="cat"
        ),
        href=url,
        is_external=True,
    )