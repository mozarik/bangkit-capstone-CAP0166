from sqlalchemy import Column, Integer, String
from .database import Base


class Preprocess(Base):
    __tablename__ = "preprocess"

    id = Column(Integer, primary_key=True, index=True)
    img_url = Column(String(255))
