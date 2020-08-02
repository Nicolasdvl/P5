from sqlalchemy import Column, String, BigInteger
from sqlalchemy.orm import relationship
from models import Base
from models import category, store


class Product(Base):
    __tablename__ = "product"

    code = Column(BigInteger, primary_key=True)
    name = Column(String(120), nullable=False)
    ingredients = Column(String(500))
    brand = Column(String(120))
    labels = Column(String(120))
    score = Column(String(1))
    categories = relationship(
        "Category", secondary=category.prod_cat, back_populates="products"
    )
    stores = relationship(
        "Store", secondary=store.prod_store, back_populates="products"
    )
