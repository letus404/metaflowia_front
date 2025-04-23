import reflex as rx
import os

config = rx.Config(
    app_name="METAFLOWIA",
    api_url="https://metaflowia.onrender.com",
)

# para despliegue en reflex deploy directo y que agregue el .env | reflex deploy --envfile .env