import reflex as rx
import new_project.styles.styles as styles


def title(text:str) -> rx.Component: 
    return rx.heading(
        text,
    )