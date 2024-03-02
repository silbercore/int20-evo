from fastapi_users import schemas
from typing import List, Optional, Union
from datetime import datetime

class UserRead(schemas.BaseUser[int]):
    id: int
    email: str
    name: str
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False
    registered_at:datetime
    role:str
    faculty:str
    group:str
    kyrs:str
    gender:str

    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    email: str
    name: str
    password: str
    registered_at:datetime
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False
    role:str
    faculty:str
    group:str
    kyrs:str
    gender:str


class UserUpdate(schemas.BaseUserUpdate):
    email: str
    name: str
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False
    faculty:str
    group:str
    kyrs:str
    gender:str