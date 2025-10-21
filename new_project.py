import reflex as rx
import reflex_local_auth
from rxconfig import config
from .ui.base import base_page
from . import blog, contact, navigation, pages, components #auth
from .views.header.header import header
from new_project.components.link_icon import link_icon
from new_project.components.link_icon import link_icon_2
from new_project.styles.styles import Size as Size
from new_project.components.info_tex import info
from new_project.styles.colors import Text_color as Text_color
from new_project.styles.colors import Color as Color



class State(rx.State):
    """The app state."""
    label = "Welcome to SoloKiamix"
 
    def handle_title_input_change(self, val):
        self.label = val
        
    def did_click_about_1(self):
        return rx.redirect(navigation.routes.PRICING_ROUTE)
    
    def did_click_about_2(self):
        return rx.redirect(navigation.routes.ODONTOLOGIA_ROUTE)


def index() -> rx.Component:
    # Welcome Page (Index)
    my_child = rx.box(
                #rx.theme_panel(default_open=True),
                rx.center(
                    rx.vstack(
                        header(),
                        rx.text(
                            """SoloKiaMix es un espacio dedicado a promover el bienestar integral, 
                            donde la nutrición y la odontología juegan un papel central. Está diseñado para ofrecer un enfoque integral hacia el bienestar, 
                            combinando asesorías personalizadas en nutrición con un compromiso con la salud y el equilibrio.
                            La filosofía del proyecto se basa en el equilibrio entre nutrición y saludn bucodental, 
                            brindando soluciones integrales para quienes buscan verse y sentirse mejor.""",
                            color="#bfa76f",
                            text_align="justify"
                            ),
                        rx.hstack(
                        ),
                        rx.button("Asesoría Nutricional", on_click=State.did_click_about_1),
                        rx.button("Consulta Odontológica", on_click=State.did_click_about_2),    
                        max_width="600px",
                        width="100%",
                        margin_y=Size.BIG.value
                        )
                ),
                rx.center(
                    components.footer(),
                ),
                spacing="5",
                justify="center",
                min_height="85vh",
                text_align="center",
                align="center",
            )
    return base_page(
            my_child
            )


app = rx.App(
    stylesheets=["/custom_brown.css"],
    theme=rx.theme(
        appearance="inherit",
        has_background=True,
        radius="large",
        accent_color="orange",
        panel_background="translucent",
    ),
)

app.add_page(index)
#app.add_page(
#    auth.pages.my_login_page,
#    route=reflex_local_auth.routes.LOGIN_ROUTE,
#    title="Login",
#)
#app.add_page(
#    auth.pages.my_register_page,
#    route=reflex_local_auth.routes.REGISTER_ROUTE,
#    title="Register",
#)
app.add_page(pages.about_page, route=navigation.routes.ABOUT_US_ROUTE)
#app.add_page(
#    pages.protected_page,
#    route="/protected/",
#    on_load=auth.SessionState.on_load
#)
app.add_page(
    blog.blog_post_list_page,
    route=navigation.routes.BLOG_POSTS_ROUTE,
    on_load=blog.BlogPostState.load_posts
    )
app.add_page(
    blog.blog_post_add_page,
    route=navigation.routes.BLOG_POSTS_ADD_ROUTE,
    )
app.add_page(
    blog.blog_post_detail_page,
    route="/blog/[blog_id]",
    on_load=blog.BlogPostState.get_post_detail
    )
app.add_page(
    blog.blog_post_edit_page,
    route="/blog/[blog_id]/edit",
    on_load=blog.BlogPostState.get_post_detail
    )
app.add_page(contact.contact_page, route=navigation.routes.CONTACT_US_ROUTE)
app.add_page(pages.odontologia_page, route=navigation.routes.ODONTOLOGIA_ROUTE)
app.add_page(pages.producto_page, route=navigation.routes.PRODUCTO_ROUTE)
app.add_page(
    contact.contact_entries_list_page,
    route=navigation.routes.CONTACT_ENTRIES_ROUTE,
    on_load=contact.ContactState.list_entries
    )
app.add_page(pages.pricing_page, route=navigation.routes.PRICING_ROUTE)


