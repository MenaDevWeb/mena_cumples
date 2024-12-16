import reflex as rx

config = rx.Config(
    app_name="mena_cumples",
    cors_allowed_origins=[
        "http://localhost:3000",
        "https://mena-cumples.vercel.app",
        "https://mena-cumples-kp2nw8r1s-menadevwebs-projects.vercel.app"
    ]
)