from sqlalchemy import Column, Integer, LargeBinary, String, ForeignKey, DateTime, Double, Enum
from sqlalchemy.orm import relationship
from datetime import datetime, timedelta
from database import Base
from auth.models import User
from enum import Enum

class Exam(Base):
    __tablename__ = "exam"

    id = Column(Integer, primary_key=True)
    mark = Column(String, nullable=False)
    date = Column(DateTime, default=datetime.utcnow())
    subject_name = Column(String)
    teacher_id = Column(Integer)
    user_id = Column(Integer)

class Leson_name(str, Enum):
    HISTORY = "HISTORY"
    MATH = "MATH"
    PHYSICS = "PHYSICS"
    INFORMATIC = "INFORMATIC"