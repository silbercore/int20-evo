from sqlalchemy import Column, Integer, LargeBinary, String, ForeignKey, DateTime, Double, Enum
from sqlalchemy.orm import relationship
from datetime import datetime, timedelta
from database import Base
from auth.models import User
from enum import Enum

class Presense(Base):
    __tablename__ = "presense"

    id = Column(Integer, primary_key=True)
    label = Column(String, nullable=False)
    date = Column(DateTime, default=datetime.utcnow())

    teacher_id = Column(Integer)
    user_id = Column(Integer)

class Label(str, Enum):
    DUTY = "DUTY"
    HOSPITAL = "HOSPITAL"
    SICK = "SICK"
    ON_LEAVE = "ON_LEAVE"