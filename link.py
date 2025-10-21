import reflex as rx

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


def link() -> rx.Component:
    return rx.vstack(
        title("Planes Dietéticos"), 
        link_button_aging(
            "Plan Anti-aging",
            """Enfocado en la protección celular y la prevención del envejecimiento, este plan ayuda a combatir los radicales libres y mejora la salud de la piel, el cabello y el sistema inmunológico.""",
            "https://www.google.com/webhp?hl=es&sa=X&ved=0ahUKEwiy5-TyvO2LAxVjBdsEHVFWB0IQPAgI",
            ),
        link_button_detox(
            "Plan Detox",
            """Ideal para depurar el organismo, eliminando toxinas acumuladas y promoviendo una digestión eficiente, este plan revitaliza el cuerpo y favorece el bienestar general.""",
            "https://www.google.com/webhp?hl=es&sa=X&ved=0ahUKEwiy5-TyvO2LAxVjBdsEHVFWB0IQPAgI"),
        link_button_weight(
            "Plan Pérdida de Peso",
            """Diseñado para aquellos que desean perder peso de manera saludable y sostenible, promoviendo una alimentación balanceada que acelere el metabolismo y reduzca el almacenamiento de grasa.""",
            "https://www.google.com/webhp?hl=es&sa=X&ved=0ahUKEwiy5-TyvO2LAxVjBdsEHVFWB0IQPAgI"),
        link_button_power(
            "Plan Power",
            """Diseñado para quienes buscan aumentar su fuerza y ganar masa muscular. Con una dieta rica en proteínas, carbohidratos complejos y grasas saludables, este plan optimiza el rendimiento físico, acelera la recuperación y favorece el crecimiento muscular.""",
            "https://www.google.com/webhp?hl=es&sa=X&ved=0ahUKEwiy5-TyvO2LAxVjBdsEHVFWB0IQPAgI"),
        link_button_baby(
            "Plan Sitaciones Especiales",
            """El embarazo y la lactancia son etapas fundamentales en la vida de una mujer que requieren una atención nutricional especializada. Cada fase trae consigo necesidades específicas para asegurar la salud de la madre y el bebé.""",
            "https://www.google.com/webhp?hl=es&sa=X&ved=0ahUKEwiy5-TyvO2LAxVjBdsEHVFWB0IQPAgI"),
        link_button_coffee(
            "Plan Feel Free",
            """Creado a medida según las necesidades específicas del usuario, teniendo en cuenta sus objetivos, condiciones de salud y preferencias alimenticias.""",
            "https://www.google.com/webhp?hl=es&sa=X&ved=0ahUKEwiy5-TyvO2LAxVjBdsEHVFWB0IQPAgI"),
        title("Recursos"), 
        link_button_utensils(
            "Alimentación Saludable",
            "Aprende a comer saludable con el plato de Harvard. Conócete y notarás las mejoras.",
            "https://www.google.com/webhp?hl=es&sa=X&ved=0ahUKEwiy5-TyvO2LAxVjBdsEHVFWB0IQPAgI"),
        link_button_pot(
            "Guía Tamaño de Porciones",
            """Aprender a medir y ajustar las porciones según tus necesidades te permitirá optimizar resultados y mantener un estilo de vida saludable.""",
            "https://www.google.com/webhp?hl=es&sa=X&ved=0ahUKEwiy5-TyvO2LAxVjBdsEHVFWB0IQPAgI"),
        title("Contacto"), 
        link_button_mail("e-mail","csolerdelvalle@gmail.com",f"mailto:csolerdelvalle@gmail.com"),
        link_button_phone("Whatsapp","Respuesta rápida","https://www.google.com/webhp?hl=es&sa=X&ved=0ahUKEwiy5-TyvO2LAxVjBdsEHVFWB0IQPAgI"),
        title("Equipo"), 
        link_button_user("Carlos Soler","Farmacéutico, Biotecnólogo y Nutricionista",f"mailto:csolerdelvalle@gmail.com"),
        link_button_user("Laura Lorente","Odontóloga Ortodoncista",f"mailto:csolerdelvalle@gmail.com"),
        width="100%"

    )