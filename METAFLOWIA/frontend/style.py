# style.py
import reflex as rx


# Sombra sutil y márgenes laterales
shadow = "0 1px 2px rgba(255, 255, 255, 0.05)"
chat_side_margin = "10%"

# Estilo base para mensajes del chat
base_message_style = dict(
    padding="8",
    border_radius="18px",
    margin="20px",
    box_shadow=shadow,
    max_width="80%",
    font_size="16px",
    line_height="1.5",
    display="inline-block",
    transition="all 0.2s ease-in-out",
)

# Estilo para preguntas del usuario (verde oscuro, alineado a la derecha)
question_style = base_message_style | dict(
    margin_left=chat_side_margin,
    padding="16px",
    background_color="#1e4435",
    color="#eaffea",
    align_self="flex-end",
    font_size="16px",
)

# Estilo para respuestas del asistente (gris oscuro, alineado a la izquierda)
answer_style = base_message_style | dict(
    margin_right=chat_side_margin,
    background_color="#2a2a2a",
    color="#f1f1f1",
    border="1px solid #3a3a3a",
    align_self="flex-start",
    padding="16px",
    font_size="14px",
)

# Estilo para input de texto
input_style = dict(
    background_color="#1e1e1e",
    border="1px solid #00ff99",
    color="#fff",
    border_radius="20px",
    padding="5px",
    margin="6px",
    height="15%",
    width="100%",
    font_size="1em",
    box_shadow="none",
)

# Estilo para botón de enviar (verde tipo WhatsApp)
button_style = dict(
    background="#003d3d",
    color="#00ff99",
    border="1px solid #00ff99",
    border_radius="xl",
    padding_x="20px",
    padding_y="12px",
    font_weight="bold",
    font_size="16px",
    _hover={
        "transform": "scale(1.05)",
    },
    _active={
        "transform": "scale(0.98)",
    },
)
