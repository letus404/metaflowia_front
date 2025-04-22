import reflex as rx
from METAFLOWIA.frontend.constants import personalities
from METAFLOWIA.frontend.state import State
#Componente para elegir personalidad
def menu_selector() -> rx.Component:
    return rx.box(
        rx.menu.root(
            rx.menu.trigger(
                rx.button(
                    f"🌐 Personalidad: {State.selected_label}",
                    color_scheme="purple",
                    variant="outline",
                    size="3",
                    margin="12px",
                    width="100%",
                ),
            ),
            rx.menu.content(
                *[
                    rx.menu.item(
                        rx.tooltip(
                            rx.text(personalities[key]["label"]),
                            content=personalities[key]["tooltip"],
                            has_arrow=True,
                            placement="right",
                        ),
                        on_click=rx.event(lambda: State.set_personality(key)),
                    )
                    for key in personalities
                ]
            ),
        ),
        width="100%",
        max_width="800px",
    )