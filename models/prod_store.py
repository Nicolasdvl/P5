from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class ProdStore (Base):
    __tablename__ = "product_store"

    id_data = Column(Integer, )
    id_store = Column(Integer, )