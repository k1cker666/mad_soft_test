from fastapi import UploadFile
from pydantic import BaseModel, ConfigDict, Field


class MemeBase(BaseModel):
    file: UploadFile
    caption: str = Field(
        ...,
        min_length=1,
        max_length=500,
        caption="Описание мема(максимум 500 символов)",
    )


class Meme(MemeBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


class MemeOut(BaseModel):
    id: int
    file_name: str
    caption: str
