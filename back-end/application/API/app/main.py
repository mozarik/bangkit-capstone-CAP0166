import hashlib
import os
import time

from fastapi import FastAPI, Depends, UploadFile, File, HTTPException
from google.cloud import storage

from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine

from extract import Extract
from entry_ml import numpyarray_to_blob

app = FastAPI()

CLOUD_STORAGE_BUCKET = os.environ.get('CLOUD_STORAGE_BUCKET')


# models.Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    # Create a Cloud Storage client.
    gcs = storage.Client()

    # Get the bucket that the file will be uploaded to.
    bucket = gcs.get_bucket(CLOUD_STORAGE_BUCKET)

    # create name file for encrypted
    name_file = file.filename + str(time.time())
    result = hashlib.md5(name_file.encode('utf-8')).hexdigest()
    # Create a new blob and upload the file's content.
    blob = bucket.blob(str(result))

    content = await file.read()
    blob.upload_from_string(
        content,
        content_type=file.content_type
    )
    blob.make_public()

    # insert to database
    model = schemas.PreprocessCreate(img_url=blob.public_url)
    create_preprocess(db=db, preprocess=model)


    extract = Extract()
    file_numpy = extract.read_image(image=blob.public_url)

    # create name file for encrypted
    name_file2 = str(time.time())
    result2 = hashlib.md5(name_file2.encode('utf-8')).hexdigest()
    # Create a new blob and upload the file's content.
    blob2 = bucket.blob(str(result))
    blob2.upload_from_string(
        file_numpy,
        content_type=file.content_type
    )
    blob2.make_public()
    return {"status": 200, "data": blob2.public_url}


@app.post("/add-preprocess/", response_model=schemas.Preprocess)
def create_preprocess(preprocess: schemas.PreprocessCreate, db: Session = Depends(get_db)):
    return crud.create_preprocess(db=db, preprocess=preprocess)


@app.post("/add-postprocess/", response_model=schemas.Postprocess)
def create_postprocess(postprocess: schemas.PostprocessCreate, db: Session = Depends(get_db)):
    return crud.create_postprocess(db=db, postprocess=postprocess)


@app.get("/postprocess/{parent_id}")
def read_postprocess(parent_id: int, db: Session = Depends(get_db)):
    db_postprocess = crud.get_postprocess(db, parent_id=parent_id)

    if db_postprocess is None:
        raise HTTPException(status_code=404, detail="Postprocess not found")
    return db_postprocess
