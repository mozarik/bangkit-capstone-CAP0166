import hashlib
import os
import time

from fastapi import FastAPI, Depends, UploadFile, File, HTTPException, BackgroundTasks
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

models.Base.metadata.create_all(bind=engine)


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
async def create_upload_file(baclground_tasks: BackgroundTasks, file: UploadFile = File(...),
                             db: Session = Depends(get_db)):
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

    # using background task
    baclground_tasks.add_task(extract_face_url, blob.public_url, file.content_type)

    # file_numpy = extract.read_image(image=blob.public_url)
    # content2 = numpyarray_to_blob(file_numpy)
    # # create name file for encrypted
    # name_file2 = str(time.time())
    # result2 = hashlib.md5(name_file2.encode('utf-8')).hexdigest()
    # # Create a new blob and upload the file's content.
    # blob2 = bucket.blob(str(result2))
    # blob2.upload_from_string(
    #     content2,
    #     content_type=file.content_type
    # )
    # blob2.make_public()
    return {"status": 200, "data": blob.public_url}


def extract_face_url(url: str, content_type):
    gcs = storage.Client()
    bucket = gcs.get_bucket(CLOUD_STORAGE_BUCKET)

    extract = Extract()
    image_of_faces = extract.image_from_url(url)
    list_of_faces = extract.extract_face_to_list(image_of_faces)

    list_url_face = []
    for i in list_of_faces:
        content_face = numpyarray_to_blob(i)
        name_face = str(time.time())
        result_face = hashlib.md5(name_face.encode('utf-8')).hexdigest()
        blob_face = bucket.blob(str(result_face))
        blob_face.upload_from_string(
            content_face,
            content_type=content_type
        )
        blob_face.make_public()
        list_url_face.append(blob_face.public_url)


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
