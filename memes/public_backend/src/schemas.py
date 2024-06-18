from pydantic import BaseModel, ConfigDict, Field


class MemeBase(BaseModel):
    file_name: str = Field(
        ...,
        min_length=4,
        max_length=20,
        caption="Название(минимум 4, максимум 20 символов)",
    )
    caption: str = Field(
        ...,
        min_length=1,
        max_length=500,
        caption="Описание мема(максимум 500 символов)",
    )


class MemeCreate(MemeBase):
    pass


class MemeUpdate(MemeBase):
    pass


class Meme(MemeBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
