import random
from typing import Annotated

from fastapi import APIRouter, Path


router = APIRouter(prefix="/memes")


@router.get("/")
def get_list_memes():
    return {"memes": "list"}


@router.get("/{id}/")
def get_meme_from_id(id: Annotated[int, Path(ge=1)]):
    memes = ["funny meme", "not funny meme", "best meme", "worst meme"]
    return {"meme": {"meme_id": id, "meme": random.choice(memes)}}


@router.post("/")
def add_new_meme(meme, caption: str):
    return {"add": "success"}


@router.put("/{id}")
def update_meme(meme):
    return {"update": "success"}


@router.delete("/{id}")
def delete_meme(meme, caption: str):
    return {"delete": "success"}
