import reflex as rx

config = rx.Config(
    app_name="mena_cumples",
    cors_allowed_origins=[
        "http://localhost:3000",
        "https://mena-cumples.vercel.app/"
    ]
)