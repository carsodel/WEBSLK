import reflex as rx
import reflex_local_auth

HOME_ROUTE="/"
ABOUT_US_ROUTE="/about"
PRICING_ROUTE="/planes"
CONTACT_US_ROUTE="/contact"
ODONTOLOGIA_ROUTE="/odontologia"
PRODUCTO_ROUTE="/producto"
CONTACT_ENTRIES_ROUTE="/contact/entries"
BLOG_POSTS_ROUTE="/blog"
BLOG_POSTS_ADD_ROUTE="/blog/add"
BLOG_POST_DETAIL_ROUTE = "/blog/post/{post_id}"
REGISTER_ROUTE_1 = reflex_local_auth.routes.REGISTER_ROUTE
LOGIN_ROUTE_1= reflex_local_auth.routes.LOGIN_ROUTE