from fastapi import APIRouter, Depends, status
from src import crud
from src.dbmanager import db_manager
from src.dependencies import meme_by_id
from src.schemas import Meme, MemeCreate, MemeUpdate


router = APIRouter(prefix="/memes", tags=["Memes"])


@router.get(
    "/",
    response_model=list[Meme],
)
def get_list_memes(session=Depends(db_manager.session_dependency)):
    return crud.get_memes(session=session)


@router.get(
    "/{id}/",
    response_model=Meme,
)
def get_meme_from_id(
    meme: Meme = Depends(meme_by_id),
):
    return meme


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


@router.put(
    "/{id}",
    response_model=Meme,
)
def update_meme(
    meme_update: MemeUpdate,
    meme: Meme = Depends(meme_by_id),
    session=Depends(db_manager.session_dependency),
):
    return crud.update_meme(
        session=session,
        meme=meme,
        meme_update=meme_update,
    )


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_meme(
    meme: Meme = Depends(meme_by_id),
    session=Depends(db_manager.session_dependency),
):
    return crud.delete_meme(session=session, meme=meme)
