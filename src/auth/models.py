from datetime import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable

from sqlalchemy import JSON, Column, Integer, String, TIMESTAMP, ForeignKey,Boolean, Table
from sqlalchemy.orm import DeclarativeBase, relationship
from database import Base, metadata


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__="user"

    id = Column(Integer, primary_key=True)
    email: str = Column(String(length=320), unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    hashed_password: str = Column(String(length=1024), nullable=False)
    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)
    role = Column(String, nullable=False)
    faculty = Column(String, nullable=False)
    group = Column(String, nullable=False)
    kyrs = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    # ivents = relationship("Ivent", secondary='user_ivent', back_populates="users")

    # bets = relationship("Bet", back_populates="user")
