import reflex as rx
from ..ui.base import base_page
from rxconfig import config
from .. import blog, contact, navigation, pages, components
from new_project.views.header.header import header
from new_project.components.link_icon import link_icon
from new_project.components.link_icon import link_icon_2
from new_project.styles.styles import Size as Size
from new_project.components.info_tex import info
from new_project.styles.colors import Text_color as Text_color
from new_project.styles.colors import Color as Color
from new_project.components.link_button import link_button
from new_project.components.link_button import link_button_detox
from new_project.components.link_button import link_button_aging
from new_project.components.link_button import link_button_power
from new_project.components.link_button import link_button_weight
from new_project.components.link_button import link_button_baby
from new_project.components.link_button import link_button_coffee
from new_project.components.link_button import link_button_mail
from new_project.components.link_button import link_button_pot
from new_project.components.link_button import link_button_user
from new_project.components.link_button import link_button_phone
from new_project.components.link_button import link_button_utensils

from new_project.components.title import title

#@rx.page(route="/about")
def odontologia_page() -> rx.Component:
    my_child = rx.box(
                #rx.theme_panel(default_open=True),
                rx.center(
                    rx.vstack(
                        title("Bienestar que se refleja en tu sonrisa"), 
                        rx.text(
                            """SoloKiaMix es un espacio dedicado a promover el bienestar integral, 
                            donde la nutrición juega un papel central. Está diseñado para ofrecer un enfoque integral hacia el bienestar, 
                            combinando asesorías personalizadas en nutrición con un compromiso con la salud y el equilibrio.
                            En el futuro, Kiamix expandirá su oferta incorporando servicios de cosmética y 
                            productos cosméticos de alta calidad, enfocados en el cuidado y la belleza desde un enfoque natural y 
                            saludable. La filosofía de Kiamix se basa en el equilibrio entre cuerpo y mente, 
                            brindando soluciones integrales para quienes buscan verse y sentirse mejor.""",
                            color=Text_color.BODY.value,
                            text_align="justify"
                            ),
                        max_width="600px",
                        width="100%",
                        margin_y=Size.BIG.value
                    ),
                ),
                    rx.center(
                        components.footer(),
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
