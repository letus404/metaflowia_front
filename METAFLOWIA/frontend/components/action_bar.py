import reflex as rx
from METAFLOWIA.frontend.state import State
from METAFLOWIA.frontend.style import input_style, button_style
# Componente para la barra de acción (input + botón)
def action_bar() -> rx.Component:
    return rx.form( 
        rx.hstack(
            rx.input(
                value=State.question,
                placeholder="¿Qué pasaría si obtuvieras lo que buscas?",
                on_change=State.set_question,
                style=input_style,
                width="70%",
            ),
            rx.button(
                "⚡ ENVIAR ⚡",
                on_click=State.answer,
                style=button_style,
            ),
            spacing="2",
            align="center",
            
        ),
        on_submit=State.answer,
        width="100%",
    )