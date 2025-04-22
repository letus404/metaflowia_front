import reflex as rx
from METAFLOWIA.frontend.state import AuthState


def login_dialog() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button("Iniciar Sesión", variant="solid", color_scheme="gray", margin_x="4px")
        ),
        rx.dialog.content(
            rx.dialog.title("Iniciar sesión", margin_bottom="12px"),
            rx.dialog.description("Ingresa tus credenciales", margin_bottom="12px"),
            rx.form(
                rx.vstack(
                    rx.input(
                        placeholder="Usuario",
                        name="username",
                        is_required=True,
                        width="100%",
                        value=AuthState.username,
                        on_change=AuthState.set_username
                    ),
                    rx.input(
                        placeholder="Contraseña",
                        name="password",
                        type_="password",
                        is_required=True,
                        width="100%",
                        value=AuthState.password,
                        on_change=AuthState.set_password
                    ),
                    rx.hstack(
                        rx.dialog.close(rx.button("Cancelar", variant="soft", color_scheme="gray")),
                        rx.button("Ingresar", type="submit", color_scheme="green"),
                        justify="end"
                    )
                ),
                on_submit=AuthState.do_login,
            ),
            max_width="400px"
        )
    )


def register_dialog() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button("Crear Cuenta", variant="outline", color_scheme="green", margin_x="4px")
        ),
        rx.dialog.content(
            rx.dialog.title("Crear nuevo usuario", margin_bottom="12px"),
            rx.dialog.description("Completa el formulario", margin_bottom="12px"),
            rx.form(
                rx.vstack(
                    rx.input(
                        placeholder="Nombre completo",
                        name="full_name",
                        width="100%",
                        value=AuthState.full_name,
                        on_change=AuthState.set_full_name
                    ),
                    rx.input(
                        placeholder="Correo electrónico",
                        name="email",
                        type_="email",
                        is_required=True,
                        width="100%",
                        value=AuthState.email,
                        on_change=AuthState.set_email
                    ),
                    rx.input(
                        placeholder="Nombre de usuario",
                        name="username",
                        is_required=True,
                        width="100%",
                        value=AuthState.register_username,
                        on_change=AuthState.set_register_username
                    ),
                    rx.input(
                        placeholder="Contraseña",
                        name="password",
                        type_="password",
                        is_required=True,
                        width="100%",
                        value=AuthState.register_password,
                        on_change=AuthState.set_register_password
                    ),
                    rx.input(
                        placeholder="Confirmar contraseña",
                        name="confirm_password",
                        type_="password",
                        is_required=True,
                        width="100%",
                        value=AuthState.confirm_password,
                        on_change=AuthState.set_confirm_password
                    ),
                    rx.hstack(
                        rx.dialog.close(rx.button("Cancelar", variant="soft", color_scheme="gray")),
                        rx.button("Registrar", type="submit", color_scheme="green"),
                        justify="end"
                    )
                ),
                on_submit=AuthState.do_register,
            ),
            max_width="500px"
        )
    )


def auth_dialogs() -> rx.Component:
    return rx.box(
        login_dialog(),
        register_dialog(),
        spacing="5",
        align="center",
        justify="center"
    )