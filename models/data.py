from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Data(Base):
    __tablename__ = "data"

    id = Column(Integer, primary_key=True)
    category = Column(String(24), nullable =False)
    name = Column(String(24), nullable=False)
    description = Column(String(300))
    product = Column(String(24))
    ingredients = Column(String(300))
    brand = Column(String(24))
    store = Column(String(24))
    labels = Column(String(50))
    score = Column(Integer)