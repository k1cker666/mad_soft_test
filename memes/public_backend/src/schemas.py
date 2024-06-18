from pydantic import BaseModel, Field


class MemeBase(BaseModel):
    caption: str = Field(
        ...,
        min_length=1,
        max_length=500,
        description="Описание мема(максимум 500 символов)",
    )


class Meme(MemeBase):
    id: int
    file_name: str
