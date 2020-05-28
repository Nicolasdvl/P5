from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Asso_data_cat(Base):
    __tablename__ = "asso_data_cat"

    id_data = Column(Integer, )
    id_cat = Column(Integer, )