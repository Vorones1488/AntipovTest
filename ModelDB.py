from sqlalchemy import Column, Integer, String, create_engine, MetaData, Boolean, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import databases
import datetime


Base = declarative_base()
DATABASE_URL = "sqlite:///mydatabase.db"
database = databases.Database(DATABASE_URL)

engin = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engin)
metadata = MetaData()


class CadastralNumbers(Base):
    __tablename__ = 'cadastrals_numbers'
    id = Column(Integer, primary_key=True)
    number = Column(String(17))
    latitude = Column(String)
    the_length = Column(String)
    request_status = Column(Boolean)
    data_time = Column(DateTime)

Base.metadata.create_all(engin)