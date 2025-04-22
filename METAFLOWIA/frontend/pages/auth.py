import reflex as rx
from METAFLOWIA.frontend.components.auth_dialogs import auth_dialogs

def auth_page() -> rx.Component:
    return rx.center(
        rx.flex(
            rx.vstack(
                rx.heading("Bienvenido a METAFLOW IA", size="7", background_image="linear-gradient(271.68deg, #6AEEA5 0.75%, #0D6AFF 88.52%)",background_clip="text", class_name="text-transparent inline-block"),
                rx.text("Iniciá sesión o registrate para continuar", size="4", color="gray", align="center"),
                auth_dialogs(),
                spacing="6",
                padding="8",
            ),
            height="auto",
            width="500px",
            margin_top="80px",
            padding="32px",
            align_items="center",
            justify_content="center",
            border_radius="20px",  # Bordes redondeados
            class_name="shadow-md",# Sombra para destacar
            bg_color="#1e1e1e",
            border="1px solid transparent",  # Borde inicial
            _hover={"border": "1px solid #6AEEA5"}, 
        ),
        min_h="100vh",
        align="center",
        justify="center",
        width="100%", 
        overflow="hidden"
    )

page = rx.page(route="/login")(auth_page)