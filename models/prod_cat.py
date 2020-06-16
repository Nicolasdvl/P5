from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class ProdCat(Base):
    __tablename__ = "product_category"

    id_data = Column(Integer, ForeignKey )
    id_cat = Column(Integer, )