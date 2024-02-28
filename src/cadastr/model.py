from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base
from datetime import datetime





class CadastralNumbers(Base):
    __tablename__ = 'cadastrals_numbers'
    id: Mapped[int] = mapped_column(primary_key=True)
    number: Mapped[str]
    latitude: Mapped[str]
    the_length: Mapped[str]
    request_status: Mapped[bool]
    data_time: Mapped[datetime] = mapped_column(default=datetime.utcnow)

