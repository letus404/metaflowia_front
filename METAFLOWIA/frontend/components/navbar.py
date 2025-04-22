import reflex as rx
# Componente NAVBAR
def navbar() -> rx.Component:
    return rx.hstack(
        rx.link("METAFLOW:IA", href="/login", class_name="no-underline text-green-400 text-lg mx-2 bold"),
        rx.spacer(),
        rx.link("👤 Quién soy", href="/", class_name="no-underline text-white text-sm mx-2"),
        rx.link("📩 Contacto", href="/contacto", class_name="no-underline text-white text-sm mx-2"),
        rx.link("🧠 Sobre el proyecto", href="/metaflow_info", class_name="no-underline text-white text-sm mx-2"),
        padding="24px",
        background_color="#383838",
        position="sticky",
        top="0",
        margin="0",
        z_index="1000",
        border_bottom="1px solid #333",
        width="100%",
    )