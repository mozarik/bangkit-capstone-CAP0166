from sqlalchemy.orm import Session

import models
import schemas


def create_preprocess(db: Session, preprocess: schemas.PreprocessCreate):
    db_preprocess = models.Preprocess(img_url=preprocess.img_url)
    db.add(db_preprocess)
    db.commit()
    db.refresh(db_preprocess)
    return db_preprocess


def get_preprocess_by_img(db: Session, img_url: str):
    return db.query(models.Preprocess).filter(models.Preprocess.img_url == img_url).first()


def get_postprocess(db: Session, parent_id: int):
    return db.query(models.Postprocess).filter(models.Postprocess.parent_id == parent_id).all()


def create_postprocess(db: Session, postprocess: schemas.PostprocessCreate):
    db_preprocess = models.Postprocess(img_url=postprocess.img_url, name=postprocess.name,
                                       percentage=postprocess.percentage,
                                       parent_id=postprocess.parent_id)
    db.add(db_preprocess)
    db.commit()
    db.refresh(db_preprocess)
    return db_preprocess


def get_postprocess_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Postprocess).offset(skip).limit(limit).all()
