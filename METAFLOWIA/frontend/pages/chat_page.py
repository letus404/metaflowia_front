import reflex as rx
from METAFLOWIA.frontend.components.navbar import navbar
from METAFLOWIA.frontend.components.personality import menu_selector
from METAFLOWIA.frontend.components.chat import chat
from METAFLOWIA.frontend.components.action_bar import action_bar
from METAFLOWIA.frontend.components.infosession import infosession
from METAFLOWIA.frontend.state import State, ChatState, AuthState


# Página principal
def chat_page() -> rx.Component:
    return rx.box(
        AuthState.is_authenticated,
        navbar(),
        rx.center(
            rx.vstack(
                rx.text(
                    "METAFLOW: chat IA",
                    background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
                    background_clip="text",
                    class_name="text-transparent inline-block",
                    font_size="50px",
                    font_weight="bold",
                    text_align="center",
                    margin="24px",
                ),
                # Descripción del proyecto
                rx.vstack(
                    rx.text(
                        "Explorá los misterios del ahora con una conversación que va más allá de lo lógico. Este chat no responde… interpreta enigmas.",
                        color="#acfa7f",
                        class_name="text-lg m-1",
                        text_align="justify",
                        max_width="800px",
                    ),
                    rx.text(
                        "Bienvenid@ a la nueva era: la inteligencia artificial ya es parte del juego. Sumate, integrala y evolucioná... o quedate viendo cómo el futuro te pasa por encima.",
                        color="white",
                        class_name="text-md m-1",
                        text_align="justify",
                        max_width="800px",
                    ),
                    spacing="4",
                    width="100%",
                    align_items="center",
                ),
                menu_selector(),
                # Caja del chat con borde y fondo
                rx.box(
                    rx.vstack(
                        chat(),
                        action_bar(),
                        rx.button(
                            "🧹 Borrar Historial",
                            on_click=State.reset_chat,
                            color_scheme="red",
                            variant="ghost",
                            font_size="14px",
                            margin_top="8px",
                            align_self="flex-end",
                        ),
                        spacing="4",
                    ),
                    border="1px solid #1DCD9F",
                    border_radius="16px",
                    padding="24px",
                    margin_top="32px",
                    width="100%",
                    max_width="1200px",
                    height="70vh%",
                    background_color="#222",  # colorcito para separar un poco
                ),
                infosession(),

                # Footer
                rx.text(
                    "© 2025 Mariano Quinteros • Hecha con REFLEX",
                    font_size="sm",
                    color="#1DCD9F",
                    text_align="center",
                    margin="24px",
                ),

                spacing="6",
                width="100%",
                align_items="center",
                justify_content="center",
                max_width="80%",
            ),
        ),
        background_color="#181818",
        min_height="100vh",
        width="100%",
        overflow_x="hidden",
    )

page = rx.page(route="/chat",  on_load=ChatState.on_load)(chat_page)