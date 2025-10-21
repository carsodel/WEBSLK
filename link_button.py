import reflex as rx
import new_project.styles.styles as styles
from new_project.styles.styles import Size as Size


def link_button_detox(title:str, body:str, url:str) -> rx.Component: 
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag="sprout",
                    width=styles.Size.SBIG.value,
                    height=styles.Size.SBIG.value,
                    margin=Size.MEDIUM.value 

                ),
                rx.vstack(
                  rx.center(
                    rx.text(title, style=styles.button_title_style),
                  ),
                  rx.text(body, style=styles.button_body_style),
                  spacing="1",
                  align_items="start",
                  margin="4px",
                  width="100%",
                ),
            ),
            width="100%",
            height="auto",
            padding_y="1em",           
            align_items="start",
            variant="soft",

        ),
        href=url,
        is_external=True,
        width="100%",
    )
def link_button_aging(title:str, body:str, url:str) -> rx.Component: 
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src="/cell-nuclei.svg",
                    width=styles.Size.SBIG.value,
                    height=styles.Size.SBIG.value,
                    margin=Size.MEDIUM.value 

                ),
                rx.vstack(
                  rx.center(
                  rx.text(title, style=styles.button_title_style),
                  ),
                  rx.text(body, style=styles.button_body_style),
                  spacing="1",
                  align_items="start",
                  margin="4px",
                  width="100%",
                ),
            ),
            width="100%",
            height="auto",
            padding_y="1em",           
            align_items="start",
        ),
        href=url,
        is_external=True,
        width="100%",
    )
def link_button(title:str, body:str, url:str) -> rx.Component: 
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag="barcode",
                    width=styles.Size.SBIG.value,
                    height=styles.Size.SBIG.value,
                    margin=Size.MEDIUM.value 

                ),
                rx.vstack(
                  rx.center(
                  rx.text(title, style=styles.button_title_style),
                  ),
                  rx.text(body, style=styles.button_body_style),
                  spacing="1",
                  align_items="start",
                  margin="4px",
                  width="100%",
                ),
            ),
            width="100%",
            height="auto",
            padding_y="1em",           
            align_items="start",
            variant="soft",

        ),
        href=url,
        is_external=True,
        width="100%",
    )
def link_button_power(title:str, body:str, url:str) -> rx.Component: 
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag="dumbbell",
                    width=styles.Size.SBIG.value,
                    height=styles.Size.SBIG.value,
                    margin=Size.MEDIUM.value 

                ),
                rx.vstack(
                  rx.center(
                  rx.text(title, style=styles.button_title_style),
                  ),
                  rx.text(body, style=styles.button_body_style),
                  spacing="1",
                  align_items="start",
                  margin="4px",
                  width="100%",
                ),
            ),
            width="100%",
            height="auto",
            padding_y="1em",           
            align_items="start",
            variant="soft",

        ),
        href=url,
        is_external=True,
        width="100%",
    )

def link_button_weight(title:str, body:str, url:str) -> rx.Component: 
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src="\weight.svg",
                    width=styles.Size.SBIG.value,
                    height=styles.Size.SBIG.value,
                    margin=Size.MEDIUM.value 

                ),
                rx.vstack(
                  rx.center(
                  rx.text(title, style=styles.button_title_style),
                  ),
                  rx.text(body, style=styles.button_body_style),
                  spacing="1",
                  align_items="start",
                  margin="4px",
                  width="100%",
                ),
            ),
            width="100%",
            height="auto",
            padding_y="1em",           
            align_items="start",

        ),
        href=url,
        is_external=True,
        width="100%",
    )

def link_button_baby(title:str, body:str, url:str) -> rx.Component: 
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag="baby",
                    width=styles.Size.SBIG.value,
                    height=styles.Size.SBIG.value,
                    margin=Size.MEDIUM.value 

                ),
                rx.vstack(
                  rx.center(
                  rx.text(title, style=styles.button_title_style),
                  ),
                  rx.text(body, style=styles.button_body_style),
                  spacing="1",
                  align_items="start",
                  margin="4px",
                  width="100%",
                ),
            ),
            width="100%",
            height="auto",
            padding_y="1em",           
            align_items="start",

        ),
        href=url,
        is_external=True,
        width="100%",
    )

def link_button_coffee(title:str, body:str, url:str) -> rx.Component: 
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag="coffee",
                    width=styles.Size.BBIG.value,
                    height=styles.Size.BBIG.value,
                    margin=Size.MEDIUM.value 

                ),
                rx.vstack(
                  rx.center(
                  rx.text(title, style=styles.button_title_style),
                  ),
                  rx.text(body, style=styles.button_body_style),
                  spacing="1",
                  align_items="start",
                  margin="4px",
                  width="100%",
                ),
            ),
            width="100%",
            height="auto",
            padding_y="1em",           
            align_items="start",
            variant="soft",

        ),
        href=url,
        is_external=True,
        width="100%",
    )
def link_button_utensils(title:str, body:str, url:str) -> rx.Component: 
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag="utensils",
                    width=styles.Size.LARGE.value,
                    height=styles.Size.LARGE.value,
                    margin=Size.MEDIUM.value 

                ),
                rx.vstack(
                  rx.center(
                  rx.text(title, style=styles.button_title_style),
                  ),
                  rx.text(body, style=styles.button_body_style),
                  spacing="1",
                  align_items="start",
                  margin="4px",
                  width="100%",
                ),
            ),
            width="100%",
            height="auto",
            padding_y="1em",           
            align_items="start",
            variant="soft",

        ),
        href=url,
        is_external=True,
        width="100%",
    )

def link_button_pot(title:str, body:str, url:str) -> rx.Component: 
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag="cooking-pot",
                    width=styles.Size.BIG.value,
                    height=styles.Size.BIG.value,
                    margin=Size.MEDIUM.value 

                ),
                rx.vstack(
                  rx.center(
                  rx.text(title, style=styles.button_title_style),
                  ),
                  rx.text(body, style=styles.button_body_style),
                  spacing="1",
                  align_items="start",
                  margin="4px",
                  width="100%",
                ),
            ),
            width="100%",
            height="auto",
            padding_y="1em",           
            align_items="start",
            variant="soft",

        ),
        href=url,
        is_external=True,
        width="100%",
    )
def link_button_mail(title:str, body:str, url:str) -> rx.Component: 
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag="mails",
                    width=styles.Size.LARGE.value,
                    height=styles.Size.LARGE.value,
                    margin=Size.MEDIUM.value 

                ),
                rx.vstack(
                  rx.center(
                  rx.text(title, style=styles.button_title_style),
                  ),
                  rx.text(body, style=styles.button_body_style),
                  spacing="1",
                  align_items="start",
                  margin="4px",
                  width="100%",
                ),
            ),
            width="100%",
            height="auto",
            padding_y="1em",           
            align_items="start",
            variant="soft",

        ),
        href=url,
        is_external=True,
        width="100%",
    )
def link_button_phone(title:str, body:str, url:str) -> rx.Component: 
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag="phone",
                    width=styles.Size.LARGE.value,
                    height=styles.Size.LARGE.value,
                    margin=Size.MEDIUM.value 

                ),
                rx.vstack(
                  rx.center(
                  rx.text(title, style=styles.button_title_style),
                  ),
                  rx.text(body, style=styles.button_body_style),
                  spacing="1",
                  align_items="start",
                  margin="4px",
                  width="100%",
                ),
            ),
            width="100%",
            height="auto",
            padding_y="1em",           
            align_items="start",
            variant="soft",

        ),
        href=url,
        is_external=True,
        width="100%",
    )
def link_button_user(title:str, body:str, url:str) -> rx.Component: 
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag="user",
                    width=styles.Size.SBIG.value,
                    height=styles.Size.SBIG.value,
                    margin=Size.MEDIUM.value 

                ),
                rx.vstack(
                  rx.center(
                  rx.text(title, style=styles.button_title_style),
                  ),
                  rx.text(
                    body,
                    style=styles.button_body_style,
                    ),
                  spacing="1",
                  align_items="start",
                  margin="4px",
                  width="100%",
                ),
            ),
            width="100%",
            height="auto",
            padding_y="1em",           
            align_items="start",
            variant="soft",

        ),
        href=url,
        is_external=True,
        width="100%",
    )

def link_button_contacto(title:str, body:str) -> rx.Component: 
    return rx.link(
        rx.button(
            rx.hstack(
                rx.vstack(
                  rx.center(
                  rx.text(title, style=styles.button_title_style),
                  ),
                  rx.text(
                    body,
                    style=styles.button_body_style,
                    ),
                  spacing="1",
                  align_items="start",
                  margin="4px",
                  width="100%",
                ),
            ),
            width="100%",
            height="auto",
            padding_y="1em",           
            align_items="start",
            variant="soft",

        ),
    )