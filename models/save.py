from sqlalchemy import Column, Integer, String, BigInteger
from models import Base


class Save (Base):
    __tablename__ = "save"

    code = Column(BigInteger, primary_key=True)
    name = Column(String(120), nullable=False, unique=True)