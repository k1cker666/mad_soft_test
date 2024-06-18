from pydantic import BaseModel


class MemeBase(BaseModel):
    title: str
    image_url: str
    description: str


class Meme(MemeBase):
    id: int
