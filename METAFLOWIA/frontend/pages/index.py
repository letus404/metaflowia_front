# METAFLOWIA/frontend/pages/index.py

import reflex as rx
from METAFLOWIA.frontend.components.navbar import navbar
from METAFLOWIA.frontend.components.tecnologias import tecnologia

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                rx.text(
                    "MARIANO QUINTEROS",
                    background_image="linear-gradient(271.68deg, #6AEEA5 0.75%, #0D6AFF 88.52%)",
                    background_clip="text",
                    class_name="text-transparent inline-block",
                    font_size="40px",
                    font_weight="bold",
                    margin_top="48px",
                    margin_bottom="4px",  
                ),
                rx.text(
                    "DESARROLLADOR FULLSTACK · FREELANCE",
                    color="#acfa7f",
                    font_size="18px",
                    font_weight="bold",
                    text_align="center",
                    max_width="800px",
                    margin_bottom="16px",
                ),
                rx.flex(
                    rx.center(
                        rx.image(
                            src="/perfil.jpg",
                            alt="Foto de Mariano Quinteros",
                            border_radius="15px 50px",
                            box_shadow="lg",
                            width=["180px", "250px", "300px"],  # Responsive
                            height="auto",
                            margin="20px",
                        )
                    ),
                    rx.center(
                        rx.text(
                            """Soy desarrollador fullstack, enfocado hoy en día en potenciar mis habilidades con Python mientras desarrollo proyectos propios que me permiten aprender en profundidad y demostrar lo que sé hacer. Vengo formándome desde 2021 de forma autodidacta y con cursos virtuales en distintas plataformas, siempre con ganas de seguir creciendo.""",
                            color="white",
                            font_size="18px",
                            text_align="justify",
                            max_width="600px",
                            padding="20px",
                        )
                    ),
                    direction=rx.breakpoints(
                        initial="column",
                        md="row",
                        lg="row",
                    ),
                    align="center",
                    justify="center",
                    width="100%",
                ),
                rx.vstack(
                    rx.text(
                        "🛠️ Tecnologías y Herramientas",
                        font_size="24px",
                        font_weight="bold",
                        color="#1DCD9F",
                        margin_bottom="16px",
                    ),
                    tecnologia("Python", "/python.png", 80),
                    tecnologia("(HTML, CSS, JS)", "/front.png", 90),
                    tecnologia("PHP", "/php.png", 65),
                    tecnologia("Tailwind", "/tailwind.png", 85),
                    tecnologia("WordPress", "/wordpress.png", 70),
                    tecnologia("Photoshop", "/photoshop.png", 70),
                    spacing="6",
                    align="center",
                    width=rx.breakpoints(
                        initial="100%",
                        md="50%",
                        lg="100%",
                    ),
                ),
                rx.text(
                    "© 2025 Mariano Quinteros • Hecha con REFLEX",
                    font_size="sm",
                    color="#1DCD9F",
                    text_align="center",
                    margin_top="20px",
                ),
            ),
            padding="20px",
            align="center",
        ),
        width="100%",
        min_height="100vh",
    )

page = rx.page(route="/")(index)






