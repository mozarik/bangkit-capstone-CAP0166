import os

from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from google.cloud import storage
app = FastAPI()

CLOUD_STORAGE_BUCKET = os.environ['CLOUD_STORAGE_BUCKET']
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

    # Create a new blob and upload the file's content.
    blob = bucket.blob(file.filename)

    blob.upload_from_string(
        file.read(),
        content_type=file.content_type
    )
    # The public URL can be used to directly access the uploaded file via HTTP.
    return blob.public_url
