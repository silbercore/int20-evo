from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from auth.auth import auth_backend, fastapi_users
from auth.schema import UserCreate, UserRead, UserUpdate
from fastapi.middleware.cors import CORSMiddleware
from pages.router import router as page_router

import ssl

app = FastAPI(title="Hack apps")

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)

app.include_router(page_router)
app.mount("/static", StaticFiles(directory="pages/static"), name="static")
app.mount("/js", StaticFiles(directory="pages/js"), name="js")

# origins = ["http://localhost:8000/","https://localhost:8000/", "http://127.0.0.1:5500", "http://64.225.5.39:8080", "http://localhost:8080"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Accept","Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"],
)

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain('../cert/cert.pem', keyfile='../cert/key.pem')