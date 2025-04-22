import reflex as rx
from METAFLOWIA.frontend.style import question_style, answer_style

# Componente para una interacción pregunta-respuesta
def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(question, style=question_style),
            text_align="right",
            width="100%",
        ),
        rx.box(
            rx.text(answer, style=answer_style),
            text_align="left",
            width="100%",
        ),
        margin_y="1",
        width="100%",
    )
