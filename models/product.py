from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Product (Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True) 
    name = Column(String(24), nullable=False)
    ingredients = Column(String(300))
    brand = Column(String(24))  
    labels = Column(String(50))
    score = Column(Integer)