import reflex as rx
from ..ui.base import base_page
from rxconfig import config
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
from .. import blog, contact, navigation, pages, components
from new_project.views.header.header import header
from new_project.components.link_icon import link_icon
from new_project.components.link_icon import link_icon_2
from new_project.styles.styles import Size as Size
from new_project.components.info_tex import info
from new_project.styles.colors import Text_color as Text_color
from new_project.styles.colors import Color as Color
import new_project.styles.styles as styles
from new_project.styles.styles import Size as Size



def pricing_page() -> rx.Component:
    my_child = rx.box(
        rx.hstack(
            rx.vstack(
                rx.box(
                    rx.center(
                        rx.image(src="/cell-nuclei.svg", width="50px", height="50px")
                    ),
                    background_color="#E6E6FA",
                    padding_y="1em",
                    padding_x="1em",
                    border_radius="10px",
                ),
                rx.text("Antiedad", text_align="center", font_family="Comfortaa-Medium"),
                align="center",  # centra contenido dentro del vstack
            ),
            rx.vstack(
                rx.box(
                    rx.center(
                        rx.image(src="/kidneys.svg", width="50px", height="50px")
                    ),
                    background_color="#B2FBA5",
                    padding_y="1em",
                    padding_x="1em",
                    border_radius="10px",
                ),
                rx.text("Salud", text_align="center", font_family="Poppins"),
                rx.text("Renal", text_align="center", font_family="Poppins"),
                align="center",
            ),
            rx.vstack(
                rx.box(
                    rx.center(
                        rx.image(src="/elderly.svg", width="50px", height="50px")
                    ),
                    background_color="#B3EBF2",
                    padding_y="1em",
                    padding_x="1em",
                    border_radius="10px",
                ),
                rx.text("+65", text_align="center", font_family="Poppins"),
                align="center",
            ),
            rx.vstack(
                rx.box(
                    rx.center(
                        rx.image(src="/colon.svg", width="50px", height="50px")
                    ),
                    background_color="#ffdcd0",
                    padding_y="1em",
                    padding_x="1em",
                    border_radius="10px",
                ),
                rx.text("Salud", text_align="center", font_family="Poppins"),
                rx.text("Digestiva", text_align="center", font_family="Poppins"),
                align="center",
            ),
            rx.vstack(
                rx.box(
                    rx.center(
                        rx.image(src="/weights.svg", width="50px", height="50px")
                    ),
                    background_color="#ffc067",
                    padding_y="1em",
                    padding_x="1em",
                    border_radius="10px",
                ),
                rx.text("Nutrición", text_align="center", font_family="Poppins"),
                rx.text("Deportiva", text_align="center", font_family="Poppins"),
                align="center",
            ),
            rx.vstack(
                rx.box(
                    rx.center(
                        rx.image(src="/diabetes-measure.svg", width="50px", height="50px")
                    ),
                    background_color="#ffd1dc",
                    padding_y="1em",
                    padding_x="1em",
                    border_radius="10px",
                ),
                rx.text("Diabetes", text_align="center", font_family="Poppins"),
                align="center",
            ),
            rx.vstack(
                rx.box(
                    rx.center(
                        rx.image(src="/weight.svg", width="50px", height="50px")
                    ),
                    background_color="#AAF0D1",
                    padding_y="1em",
                    padding_x="1em",
                    border_radius="10px",
                ),
                rx.text("Pérdida", text_align="center", font_family="Poppins"),
                rx.text("Peso", text_align="center", font_family="Poppins"),
                align="center",
            ),
            rx.vstack(
                rx.box(
                    rx.center(
                        rx.image(src="/ancv.svg", width="50px", height="50px")
                    ),
                    background_color="#FADADD",
                    padding_y="1em",
                    padding_x="1em",
                    border_radius="10px",
                ),
                rx.text("Embarazo", text_align="center", font_family="Poppins"),
                rx.text("Lactancia", text_align="center", font_family="Poppins"),
                align="center",
            ),
            rx.vstack(
                rx.box(
                    rx.center(
                        rx.image(src="/heart-organ.svg", width="50px", height="50px")
                    ),
                    background_color="#ff9e8f",
                    padding_y="1em",
                    padding_x="1em",
                    border_radius="10px",
                ),
                rx.text("Salud", text_align="center", font_family="Poppins"),
                rx.text("Cardiovascular", text_align="center", font_family="Poppins"),
                align="center",
            ),
            rx.text("Cada cuerpo tiene necesidades únicas. Por eso, ofrecemos un asesoramiento personalizado a distintas etapas de la vida, objetivos personales y condiciones específicas. Descubre cuál se ajusta mejor a ti.", text_align="center", font_family="Poppins", max_width="50%", font_size ="1.5em", padding_y="1.5em"),
            spacing="2",
            align_items="flex-start",
            flex_wrap="wrap",
            align="center",
            justify="center",
            padding_y="2.5em",
            padding_x="0.75em",
        ),
        rx.box(
            rx.center(
                rx.vstack(
                    rx.text(rx.code("Asesoramiento en"),font_size ="1.5em" ),
                    link_button_aging(
                        "Plan Anti-Edad",
                        """Enfocado en la protección celular y la prevención del envejecimiento, este plan ayuda a combatir los radicales libres y mejora la salud de la piel, el cabello y el sistema inmunológico""",
                        "https://www.google.com/"
                    ),
                    link_button_detox(
                        "Plan Salud Renal",
                        """Ideal para prevenir el deterioro renal y el acúmulo de toxinas en el organismo""",
                        "https://www.google.com/"
                    ),
                    link_button_weight(
                        "Plan Pérdida de Peso",
                        """Diseñado para aquellos que desean perder peso de manera saludable y sostenible, promoviendo una alimentación balanceada que acelere el metabolismo y reduzca el almacenamiento de grasa.""",
                        "https://www.google.com/"
                    ),
                    link_button_power(
                        "Plan Power",
                        """Diseñado para quienes buscan aumentar su fuerza y ganar masa muscular. Con una dieta rica en proteínas, carbohidratos complejos y grasas saludables, este plan optimiza el rendimiento físico, acelera la recuperación y favorece el crecimiento muscular.""",
                        "https://www.google.com/"
                    ),
                    link_button_baby(
                        "Plan Situaciones Especiales",
                        """El embarazo y la lactancia son etapas fundamentales en la vida de una mujer que requieren una atención nutricional especializada. Cada fase trae consigo necesidades específicas para asegurar la salud de la madre y el bebé.""",
                        "https://www.google.com/"
                    ),
                    link_button_coffee(
                        "Plan Feel Free",
                        """Creado a medida según las necesidades específicas del usuario, teniendo en cuenta sus objetivos, condiciones de salud y preferencias alimenticias.""",
                        "https://www.google.com/"
                    ),
                    max_width="600px",
                    spacing="4",
                    width="100%",
                    margin_y=Size.BIG.value,
                )
            )
        ),
        rx.center(
            components.footer()
        )
    )

    return base_page(my_child)
