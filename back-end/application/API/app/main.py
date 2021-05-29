import os
import hashlib
import time
from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from google.cloud import storage

app = FastAPI()

CLOUD_STORAGE_BUCKET = os.environ.get('CLOUD_STORAGE_BUCKET')


class Profile(BaseModel):
    name: str
    status: Optional[str] = None
    agama: str
    TTL: datetime
    golonganDarah: str
    pekerjaan: Optional[str] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/profile/create/")
def create_profile(profile: Profile):
    return profile


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
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
    # The public URL can be used to directly access the uploaded file via HTTP.
    return {"status": 200, "data": blob.public_url}
