from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Session

from schemas import PreprocessCreate, PostprocessCreate
from database import Base


class Preprocess(Base):
    __tablename__ = "preprocess"

    id = Column(Integer, primary_key=True)
    img_url = Column(String(255))

    # children = relationship("postprocess")


class Postprocess(Base):
    __tablename__ = "postprocess"
    id = Column(Integer, primary_key=True)
    img_url = Column(String(255))
    data_predict = Column(String(255))
    parent_id = Column(Integer, ForeignKey('preprocess.id'))
