from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, BigInteger

Base = declarative_base()

class Category (Base):
    __tablename__ = "category"

    code = Column(BigInteger, primary_key =True)
    name = Column(String(60), nullable =False, unique =True)