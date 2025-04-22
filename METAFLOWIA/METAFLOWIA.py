
import reflex as rx
import os
import sys
from rxconfig import config
from METAFLOWIA.frontend.pages import index, chat_page, auth, contacto, metaflow_info

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

app = rx.App(
    style={
        "global": {
            "*": {
                "box-sizing": "border-box",
            },
            "body": {
                "margin": "0",
                "padding": "0",
                "overflow_x": "hidden",
            },
        },
    },
)

app.add_page(index, route="/", title="PERFIL DE MARIANO QUINTEROS")
app.add_page(chat_page, route="/chat", title="METAFLOW IA")
app.add_page(auth, route="/login", title="Login y Registro de usuarios") 
app.add_page(contacto, route="/contacto", title="Encuentrame")
app.add_page(metaflow_info, route="/metaflow_info", title="Sobre METAFLOW:IA")