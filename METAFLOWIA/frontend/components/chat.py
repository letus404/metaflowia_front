import reflex as rx
from METAFLOWIA.frontend.state import State
from METAFLOWIA.frontend.components.question_answer import qa

#HISTORIAL DE CHAT
def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            State.chat_history,
            lambda messages: qa(messages[0], messages[1]),
        ),
        padding="2",
        width="100%",
        class_name="max-h-[200px] md:max-h-[400px] overflow-y-auto",
    )