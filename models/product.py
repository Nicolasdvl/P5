from sqlalchemy import Table, ForeignKey, Column, Integer, String, BigInteger
from sqlalchemy.orm import relationship
from models import Base
from models import category, store

class Product (Base):
    __tablename__ = "product"

    code = Column(BigInteger, primary_key=True) 
    name = Column(String(60), nullable=False)
    ingredients = Column(String(300))
    brand = Column(String(24))  
    labels = Column(String(50))
    score = Column(String(1))
    categories = relationship(
        "Category",
        secondary=category.prod_cat,
        back_populates="products"
    )
    stores = relationship(
        "Store",
        secondary=store.prod_store,
        back_populates="products"
    )
    