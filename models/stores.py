from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Stores (Base):
    __tablename__ = "stores"

    id = Column(Integer, primary_key =True)
    name = Column(String(24))