from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path, status
from src import crud
from src.dbmanager import db_manager
from src.schemas import Meme, MemeCreate


router = APIRouter(prefix="/memes")


@router.get("/", response_model=list[Meme])
def get_list_memes(session=Depends(db_manager.session_dependency)):
    return crud.get_memes(session=session)


@router.get("/{id}/", response_model=Meme)
def get_meme_from_id(
    id: Annotated[int, Path(ge=1)],
    session=Depends(db_manager.session_dependency),
):
    meme = crud.get_meme(session=session, id=id)
    if meme is not None:
        return meme
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Meme {id} not found"
    )


@router.post(
    "/",
    response_model=Meme,
    status_code=status.HTTP_201_CREATED,
)
def create_meme(
    meme_in: MemeCreate,
    session=Depends(db_manager.session_dependency),
):
    return crud.create_meme(session=session, meme_in=meme_in)


@router.put("/{id}")
def update_meme(
    meme,
    session=Depends(db_manager.session_dependency),
):
    return {"update": "success"}


@router.delete("/{id}")
def delete_meme(
    meme,
    caption: str,
    session=Depends(db_manager.session_dependency),
):
    return {"delete": "success"}
