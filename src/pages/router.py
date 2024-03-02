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
def get_base_page(request: Request, user: User = Depends(current_user)):
    return templates.TemplateResponse("index.html", {"request": request, "user":user})

@router.get("/login")
def get_base_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.get("/tests")
def get_base_page(request: Request):
    return templates.TemplateResponse("tests.html", {"request": request})

@router.get("/raitings")
def get_base_page(request: Request):
    return templates.TemplateResponse("raitings.html", {"request": request})

@router.get("/students")
def get_base_page(request: Request):
    return templates.TemplateResponse("student.html", {"request": request})
