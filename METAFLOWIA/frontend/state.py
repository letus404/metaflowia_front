import os

import httpx
import reflex as rx
from reflex import redirect, window_alert
from dotenv import load_dotenv
from openai import OpenAI

from METAFLOWIA.frontend.constants import personalities

# ---------- CONFIGURACIÓN GENERAL ----------
load_dotenv()
backend_url = os.getenv("BACKEND_URL", "https://metaflowia.onrender.com")

# Cliente OpenAI (OpenRouter)
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)

# ---------- STATE DEL CHAT CON IA ----------
class State(rx.State):
    question: str = ""
    chat_history: list[tuple[str, str]] = []
    selected_personality: str = "neutral"

    @rx.event
    async def answer(self):
        # Append pregunta pendiente
        self.chat_history.append((self.question, ""))
        user_input = self.question
        self.question = ""
        yield

        context = personalities[self.selected_personality]["context"]
        try:
            res = client.chat.completions.create(
                model="meta-llama/llama-4-maverick:free",
                messages=[
                    {"role": "system", "content": context},
                    {"role": "user", "content": user_input},
                ],
                temperature=0.7,
                max_tokens=15_000,
            )
            answer = res.choices[0].message.content
            self.chat_history[-1] = (user_input, answer)
        except Exception as e:
            self.chat_history[-1] = (user_input, f"[Error]: {e}")
        yield

    @rx.event
    def reset_chat(self):
        self.chat_history = []
        yield

    @rx.event
    def set_question(self, value: str):
        self.question = value
        yield

    @rx.event
    def set_personality(self, key: str):
        self.selected_personality = key
        yield

    @rx.var
    def selected_label(self) -> str:
        return personalities[self.selected_personality]["label"]

    @rx.var
    def selected_context(self) -> str:
        return personalities[self.selected_personality]["context"]


# ---------- STATE DE AUTENTICACIÓN Y REGISTRO ----------
class AuthState(rx.State):
    # Login / token
    username: str = ""
    password: str = ""
    token: str = rx.LocalStorage(name="token", sync=True)
    error: str = ""

    # Registro
    full_name: str = ""
    email: str = ""
    confirm_password: str = ""
    register_username: str = ""
    register_password: str = ""
    success: str = ""

    @rx.var
    def is_authenticated(self) -> bool:
        return bool(self.token)

    # --- Setters comunes ---
    @rx.event
    def set_username(self, v: str):
        self.username = v
        yield

    @rx.event
    def set_password(self, v: str):
        self.password = v
        yield

    @rx.event
    def set_full_name(self, v: str):
        self.full_name = v
        yield

    @rx.event
    def set_email(self, v: str):
        self.email = v
        yield

    @rx.event
    def set_confirm_password(self, v: str):
        self.confirm_password = v
        yield

    @rx.event
    def set_register_username(self, v: str):
        self.register_username = v
        yield

    @rx.event
    def set_register_password(self, v: str):
        self.register_password = v
        yield

    # --- Login ---
    @rx.event
    async def do_login(self):
        async with httpx.AsyncClient() as client:
            try:
                r = await client.post(
                    f"{backend_url}/users/login",
                    data={"username": self.username, "password": self.password},
                    headers={"Content-Type": "application/x-www-form-urlencoded"},
                )
                if r.status_code == 200:
                    self.token = r.json()["access_token"]
                    self.error = ""
                    yield redirect("/chat")
                else:
                    self.error = "Credenciales inválidas"
                    yield window_alert(self.error)
            except Exception as e:
                self.error = f"Error de conexión: {e}"
                yield window_alert(self.error)

    # --- Register ---
    @rx.event
    async def do_register(self):
        if self.register_password != self.confirm_password:
            self.error = "Las contraseñas no coinciden"
            yield window_alert(self.error)
            return
        async with httpx.AsyncClient() as client:
            try:
                r = await client.post(
                    f"{backend_url}/users/register",
                    json={
                        "username": self.register_username,
                        "full_name": self.full_name,
                        "email": self.email,
                        "password": self.register_password,
                        "confirm_password": self.confirm_password
                    },
                )
                if r.status_code == 200:
                    self.success = "✅ Usuario creado con éxito. Podés iniciar sesión."
                    yield window_alert(self.success)
                    yield redirect("/login")
                else:
                    self.error = "Error al registrar usuario"
                    yield window_alert(self.error)
            except Exception as e:
                self.error = f"Error de conexión: {e}"
                yield window_alert(self.error)

    # --- Logout ---
    @rx.event
    def logout(self):
        self.token = ""
        self.username = ""
        yield redirect("/login")


# ---------- STATE DE PROTECCIÓN DE RUTAS (CHAT) ----------
class ChatState(rx.State):
    token: str = rx.LocalStorage(name="token", sync=True)

    @rx.event
    def on_load(self):
        if not self.token:
            yield redirect("/login")