from typing import List
from fastapi import APIRouter, Depends, HTTPException
from database import get_async_session, async_session_maker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import desc, select, func, delete
from auth.models import User
from exams.models import Exam
from exams.schema import UserMark
from main import fastapi_users
from datetime import datetime



current_user = fastapi_users.current_user()

router = APIRouter(
    prefix="/exam",
    tags=["Journal"]
)

current_user = fastapi_users.current_user()

@router.get("/", status_code=200)
async def get_exams(faculty:str, group:str, kyrs:str, subject_name:str, session:AsyncSession = Depends(get_async_session), user:User = Depends(current_user)):
    if not (user.role == "teacher"):
        raise HTTPException(status_code=403, detail="You are not teacher")
    
    query = (
        select(Exam, User.name)
        .join(User, User.id == Exam.user_id)
        .filter(
            User.faculty == faculty,
            User.group == group,
            User.kyrs == kyrs,
            Exam.subject_name == subject_name
        )
    )
    exams = await session.execute(query)
    exam_user_records = []
    for exam, user_name in exams.fetchall():
        exam_dict = {
            "id": exam.id,
            "mark": exam.mark,
            "date": exam.date,
            "subject_name": exam.subject_name,
            "teacher_id": exam.teacher_id,
            "user_id": exam.user_id,
            "user_name": user_name
        }
        exam_user_records.append(exam_dict)
    return exam_user_records


@router.get("/my", status_code=200)
async def get_exams(session:AsyncSession = Depends(get_async_session), user:User = Depends(current_user)):
    if not user:
        raise HTTPException(status_code=403, detail="Not authorized")

    if not (user.role == "student"):
        raise HTTPException(status_code=403, detail="You are not student")
    # query = select(Exam, User.name).join(User, Exam.teacher_id == User.id).where(Exam.user_id == user.id)
    # exams = await session.execute(query)
    # exams = await session.execute(select(Exam).where(Exam.user_id == user.id))
    # records = exams.scalars().all()
    query = (
        select(Exam, User.name)
        .join(User, Exam.teacher_id == User.id)
        .where(Exam.user_id == user.id)
    )
    result = await session.execute(query)
    records = result.fetchall()
    exam_records = []
    for exam, teacher_name in records:
        exam_dict = exam.__dict__
        exam_dict['teacher_name'] = teacher_name
        exam_records.append(exam_dict)
    return exam_records
    # records = exams.fetchall()
    # return records

@router.get("/{user_id}}", status_code=200)
async def get_exams(user_id:int, session:AsyncSession = Depends(get_async_session), user:User = Depends(current_user)):
    if not user:
        raise HTTPException(status_code=403, detail="Not authorized")

    if not (user.role == "teacher"):
        raise HTTPException(status_code=403, detail="You are not teacher")
    
    exams = await session.execute(select(Exam).where(Exam.user_id == user_id))
    records = exams.scalars().all()
    return [
        {"exam": exam, "teacher_name": teacher_name} 
        for exam, teacher_name in records
    ]

@router.post("/put_marks", status_code=201)
async def create_marks(exam_date:datetime, subject_name:str,userids_marks:List[UserMark], user: User = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    if not user:
        raise HTTPException(status_code=403, detail="Not authorized")

    if not (user.role == "teacher"):
        raise HTTPException(status_code=403, detail="You are not teacher")
    
    exams_to_add = []
    for el in userids_marks:
        new_exam = Exam(
            mark = el.mark,
            date=exam_date.replace(tzinfo=None),
            subject_name=subject_name,
            teacher_id=user.id,
            user_id=el.user_id
        )
        exams_to_add.append(new_exam)

    
    session.add_all(exams_to_add)
    await session.commit()
    return 201


