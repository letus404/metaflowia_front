import reflex as rx
from METAFLOWIA.frontend.components.navbar import navbar

def redes(icono: str) -> rx.Component:
    return rx.hstack(
        rx.image(src=icono, width="90px", height="90px"),
        spacing="2",
        width="100%",
    )

def contacto() -> rx.Component:
    return rx.box(
        navbar(),

        # Contenedor principal
        rx.flex(
            # Sección de la card centrada horizontal y verticalmente
            rx.flex(
                rx.box(
                    rx.vstack(
                        rx.heading(
                            "CONTACTO",
                            size="6",
                            background_image="linear-gradient(271.68deg, #6AEEA5 0.75%, #0D6AFF 88.52%)",
                            background_clip="text",
                            class_name="text-transparent inline-block text-4xl font-bold"
                        ),
                        rx.text(
                            "Podés encontrarme o escribirme a través de estos medios:",
                            size="4"
                        ),
                        rx.hstack(
                            rx.link(redes("/correo-electronico.png"), href="mailto:mariano.quinterosluszni@gmail.com", is_external=True),
                            rx.link(redes("/whatsapp.png"), href="https://wa.me/573137990079", is_external=True),
                            rx.link(redes("/linkedin.png"), href="https://www.linkedin.com/in/mariano-quinteros-b5448194/", is_external=True),
                            rx.link(redes("/github.png"), href="https://github.com/letus404", is_external=True),
                            spacing="4",
                        ),
                        spacing="4",
                        align="center",
                        margin="20px",
                    ),
                    width="100%",
                    max_width="1200px",
                    padding="6",
                    background_color="#383838",
                    border_radius="20px",
                    shadow="md",
                    _hover={"border": "1px solid #6AEEA5"},
                    flex="1",
                ),
                align="center",
                justify="center",
                width="100%",
                height="100%",
            ),

            # Mapa
            rx.box(
                rx.el.iframe(
                    src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d52620.040864597904!2d-75.53227049786904!3d5.060468700863743!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8e476ffa6a42ce3b%3A0xa863cf6423ea141c!2sManizales%2C%20Caldas!5e0!3m2!1ses!2sco!4v1745255644144!5m2!1ses!2sco",
                    width="100%",
                    height="30vh",
                    style={"border": 0},
                    loading="lazy"
                ),
                rx.text(
                    "© 2025 Mariano Quinteros • Hecha con REFLEX",
                    font_size="sm",
                    color="#1DCD9F",
                    text_align="center",
                    margin="12px",
                ),
                width="100%",
                flex_shrink="0",
            ),

            direction="column",
            height="90vh",
            width="100%",
        ),
        width="100%",
        overflow_y="hidden",
    )

page = rx.page(route="/contacto")(contacto)
