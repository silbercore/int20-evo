import requests
from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from auth.models import User
from main import fastapi_users
current_user = fastapi_users.current_user()

router = APIRouter(
    tags=["Pages"]
)

templates = Jinja2Templates(directory="pages/templates")

@router.get("/")
def get_base_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.get("/login")
def get_base_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.get("/students")
def get_base_page(request: Request):
    return templates.TemplateResponse("student.html", {"request": request})