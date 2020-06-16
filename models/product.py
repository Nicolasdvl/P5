from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, BigInteger

Base = declarative_base()

class Product (Base):
    __tablename__ = "product"

    code = Column(BigInteger, primary_key=True) 
    name = Column(String(60), nullable=False)
    ingredients = Column(String(300))
    brand = Column(String(24))  
    labels = Column(String(50))
    score = Column(String(1))