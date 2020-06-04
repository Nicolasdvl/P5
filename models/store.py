from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Store (Base):
    __tablename__ = "store"

    id = Column(Integer, primary_key =True)
    name = Column(String(24))