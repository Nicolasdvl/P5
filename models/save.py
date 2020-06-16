from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, BigInteger

Base = declarative_base()

class Save (Base):
    __tablename__ = "save"

    code = Column(BigInteger, primary_key=True)