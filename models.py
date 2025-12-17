from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID
import uuid
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, index=True)
    age = Column(Integer)
    phone_number = Column(String)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
