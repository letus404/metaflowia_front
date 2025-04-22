import reflex as rx
#COMPONENTE TECNOLOGIAS
def tecnologia(nombre: str, icono: str, progreso: int) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.image(src=icono, width="30px", height="30px"),
            rx.text(nombre, color="white", font_size="16px"),
            spacing="2",
        ),
        rx.progress(value=progreso, width="100%", color="#1DCD9F"),
        spacing="1",
        width="100%",
    )
