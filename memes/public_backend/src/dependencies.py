from typing import Annotated

from fastapi import Depends, HTTPException, Path, status
from src import crud
from src.dbmanager import db_manager


def meme_by_id(
    id: Annotated[int, Path(ge=1)],
    session=Depends(db_manager.session_dependency),
):
    meme = crud.get_meme(session=session, id=id)
    if meme is not None:
        return meme
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Meme {id} not found"
    )
