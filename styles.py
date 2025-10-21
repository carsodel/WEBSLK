import reflex as rx
from enum import Enum
from .colors import Color as Color
from .colors import Text_color as Text_color
from .fonts import Font as Font


MAX_WIDTH="600px"

class Size(Enum):
    SMALL="0.5em"
    MEDIUM="0.8em"
    DEFAULT="1em"
    LARGE="1.5em"
    BIG="2em"
    BBIG="2.5em"
    SBIG="3.5em"

BASE_STYLE={
    "font_family": Font.DEFAULT.value,
    "background_color": Color.BACKGROUND.value,
    rx.heading:{
         "color": Text_color.BODY.value,
         "font_family": Font.LOGO.value,
    },
    rx.button:{
        "width":"100%",
        "height":"100%",
        "display":"block",
        "padding":Size.SBIG.value,
        "border_radius":Size.SBIG.value,
        "color": Text_color.HEADER.value,
        "background_color": Color.CONTENT.value,
        "_hover":{
            "background_color": Color.SECONDARY.value,
        }

    },
    rx.link:{
        "text_decoration":"none",
        "_hover":{}
    }

}


nav_bar_style =dict(
        font_family=Font.LOGO.value,
        font_size=Size.LARGE.value

)

title_style =dict(
        width="100%",
        padding_top=Size.DEFAULT.value,
)

button_title_style = dict(
    font_family=Font.TITLE.value,
    font_size=Size.BIG.value,
    color=Text_color.HEADER.value,

)

button_body_style = dict(
    font_size=Size.DEFAULT.value,
    color=Text_color.BODY.value,


)