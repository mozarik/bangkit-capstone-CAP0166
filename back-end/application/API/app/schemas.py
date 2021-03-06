from pydantic.main import BaseModel


class Preprocess(BaseModel):
    img_url: str

    class Config:
        orm_mode = True


class PreprocessCreate(Preprocess):
    pass


class Postprocess(BaseModel):
    img_url: str
    name: str
    percentage: str
    parent_id: int

    class Config:
        orm_mode = True


class PostprocessCreate(Postprocess):
    pass