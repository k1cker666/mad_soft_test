from typing import Annotated

from fastapi import Depends, HTTPException, Path, status
from sqlalchemy import select
from sqlalchemy.orm import Session
from src import crud
from src.dbmanager import db_manager
from src.models import Meme


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


def is_meme_name_available(
    meme_name: str,
    session: Session = Depends(db_manager.session_dependency),
):
    stmt = select(Meme).filter_by(file_name=meme_name)
    result = session.execute(stmt)
    meme = result.one_or_none()
    if meme is None:
        return
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=f"Meme {meme_name} already exists",
    )
