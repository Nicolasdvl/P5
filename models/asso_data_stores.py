from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Asso_data_stores(Base):
    __tablename__ = "asso_data_stores"

    id_data = Column(Integer, )
    id_store = Column(Integer, )