import reflex as rx
from METAFLOWIA.frontend.state import AuthState
# Componente NAVBAR
def infosession() -> rx.Component:
    return rx.hstack(
    rx.text(f"👋 Hola, {AuthState.username}"),
    rx.spacer(),
    rx.button("Cerrar sesión", on_click=AuthState.logout, color_scheme="green", size="1"),
)
