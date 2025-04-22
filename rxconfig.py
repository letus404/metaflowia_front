import reflex as rx
import os

config = rx.Config(
    app_name="METAFLOWIA",
    env=rx.Env.PROD,
    port=int(os.environ.get("PORT", 3000)),
)