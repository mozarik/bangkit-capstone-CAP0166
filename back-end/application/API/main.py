from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

app = FastAPI()


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
