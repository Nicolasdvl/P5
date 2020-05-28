from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Categories (Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key =True)
    name = Column(String(24), nullable =False)