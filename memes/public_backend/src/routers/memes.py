from typing import Annotated

from fastapi import APIRouter, HTTPException, Path, status
from src import crud
from src.schemas import Meme, MemeCreate


router = APIRouter(prefix="/memes")


@router.get("/", response_model=list[Meme])
def get_list_memes(session):
    return crud.get_memes(session=session)


@router.get("/{id}/", response_model=Meme)
def get_meme_from_id(session, id: Annotated[int, Path(ge=1)]):
    meme = crud.get_meme(session=session, id=id)
    if meme is not None:
        return meme
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Meme {id} not found"
    )


@router.post("/", response_model=Meme)
def create_meme(session, meme_in: MemeCreate):
    return crud.create_meme(session=session, meme_in=meme_in)


@router.put("/{id}")
def update_meme(meme):
    return {"update": "success"}


@router.delete("/{id}")
def delete_meme(meme, caption: str):
    return {"delete": "success"}
