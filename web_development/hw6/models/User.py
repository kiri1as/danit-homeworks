from sqlalchemy import String, Integer, Sequence
from sqlalchemy.orm import Mapped, mapped_column

from .BaseModel import BaseModel


class User(BaseModel):
    __tablename__ = "users"
    user_id: Mapped[int] = mapped_column(Integer, Sequence('user_seq', start=1, increment=1), primary_key=True)
    username: Mapped[str] = mapped_column(String(40), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(60), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(24), nullable=False)
