# METAFLOWIA/frontend/pages/about_project.py

import reflex as rx
from METAFLOWIA.frontend.components.navbar import navbar  # Importá tu navbar

def acerca_del_proyecto() -> rx.Component:
    return rx.box(
        navbar(),  # Navbar normal
        rx.center(
            rx.vstack(
                rx.heading(
                    "SOBRE EL PROYECTO METAFLOW:IA",
                    size="6",
                    margin="20px",
                    background_image="linear-gradient(to right, #0D6AFF, #6AEEA5)",
                    background_clip="text",
                    class_name="text-transparent inline-block text-4xl font-bold",
                ),
                rx.flex(
                    rx.markdown(
                        """
                        ### 💬 ChatApp con sistema de usuarios

                        Este proyecto es una aplicación de chat en tiempo real desarrollada con **FastAPI** y **Reflex**, con autenticación y manejo de usuarios integrado.

                        ---

                        ### 🚀 Funcionalidades principales

                        - Registro y login de usuarios con JWT
                        - Panel de chat con mensajes en tiempo real consumiendo la api de **OPENROUTER**, utilizando el modelo: meta-llama/llama-4-maverick:free
                        - Interface responsive, moderna y fácil de usar
                        - Frontend construido completamente en Python con **Reflex**
                        - Backend robusto y escalable con **FastAPI**
                        - Almacenamiento de usuarios y mensajes en **MYSQL**

                        ---

                        ### 🧠 Objetivo del proyecto

                        El propósito principal es demostrar el flujo completo de una aplicación fullstack: desde la autenticación, creación y protección de rutas, hasta la interacción entre frontend y backend. Además, sirve como base para futuros desarrollos más complejos con sockets y funcionalidades sociales.

                        ---

                        ### 🔧 Tecnologías

                        - **FastAPI** (backend)
                        - **MYSQL** (base de datos)
                        - **Reflex** (frontend en Python)
                        - **JWT** (autenticación segura)
                        """,
                        width="100%",
                        max_width="800px",
                        padding="2rem",
                        border_radius="15px",
                        _hover={"border": "1px solid #6AEEA5"}
                    ),
                    rx.image(
                        src="/demo-proyecto.png",  
                        alt="Demo del proyecto Metaflow:IA",
                        width="100%",
                        max_width="600px",
                        border_radius="10px",
                        flex="2",
                        _hover={"border": "1px solid #6AEEA5"}
                    ),
                align="center",
                justify="center",
                direction=rx.breakpoints(
                    initial="column",
                    md="row",
                    lg="row",
                )
                ),
            align="center",
            margin="10px",
            ),
        ),
        rx.text(
                    "© 2025 Mariano Quinteros • Hecha con REFLEX",
                    font_size="sm",
                    color="#1DCD9F",
                    text_align="center",
                    margin_top="20px",
                ),
    width="100%",
    height="100vh",
    )

page = rx.page(route="/metaflow_info")(acerca_del_proyecto)