from pydantic import BaseModel


class Preprocess(BaseModel):
    id: int
    img_url: str

    class Config:
        orm_mode = True
