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


def create_preprocess(db: Session, preprocess: PreprocessCreate):
    db_preprocess = Preprocess(img_url=preprocess.img_url)
    db.add(db_preprocess)
    db.commit()
    db.refresh(db_preprocess)
    return db_preprocess


def create_postprocess(db: Session, postprocess: PostprocessCreate):
    db_preprocess = Postprocess(img_url=postprocess.img_url)
    db.add(db_preprocess)
    db.commit()
    db.refresh(db_preprocess)
    return db_preprocess