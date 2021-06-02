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
from predict import Predict
import logging

app = FastAPI()

CLOUD_STORAGE_BUCKET = os.environ.get('CLOUD_STORAGE_BUCKET')

# models.Base.metadata.create_all(bind=engine)

# config predict
pkl_path = os.environ.get('PICKL_PATH')
model_path = os.environ.get('PATH_MODEL')
predict = Predict(
    pkl_path=os.path.join(os.getcwd(), "encodings-demo.pkl"),
    model_path=os.path.join(os.getcwd(), "facenet_keras_weights.h5")
)


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
async def create_upload_file(background_tasks: BackgroundTasks, file: UploadFile = File(...),
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
    background_tasks.add_task(extract_face_url, blob.public_url, file.content_type, db)

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


def extract_face_url(url: str, content_type, db: Session):
    logging.basicConfig(level=logging.DEBUG)
    gcs = storage.Client()
    bucket = gcs.get_bucket(CLOUD_STORAGE_BUCKET)

    extract = Extract()
    image_of_faces = extract.image_from_url(url)
    list_of_faces = extract.extract_face_to_list(image_of_faces)
    logging.debug(len(list_of_faces))
    # tambah fungsi predict for i in list_of_faces
    # list of dict
    list_data = []
    for i in list_of_faces:
        data = predict.predict_face(i)
        list_data.append(data[0])
        logging.debug(data)

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

    data = db.query(models.Preprocess).filter(models.Preprocess.img_url == url).first()
    id = data.id
    logging.debug(data)

    for i in range(len(list_data)):
        model = schemas.PostprocessCreate(
            img_url=list_url_face[i],
            name=list_data[i]['name'],
            percentage=list_data[i]['percentage'],
            parent_id=id
        )
        create_postprocess(db=db, postprocess=model)


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
    return {"status": 200, "data": db_postprocess}
