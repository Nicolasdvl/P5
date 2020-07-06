from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, ForeignKey, Column, Integer, String, BigInteger
from sqlalchemy.orm import relationship
from models import Base
from models import product


prod_store = Table('prod_store', Base.metadata,
    Column('prod_id', BigInteger, ForeignKey('product.code')),
    Column('store_id', Integer, ForeignKey('store.code'))
    )

class Store (Base):
    __tablename__ = "store"

    code = Column(Integer, autoincrement=True, primary_key =True)
    name = Column(String(60), nullable =False, unique= True)
    products = relationship(
        "Product",
        secondary=prod_store,
        back_populates="stores"
    )