from typing import Annotated

from fastapi import (
    APIRouter,
    Depends,
    Form,
    Query,
    Response,
    UploadFile,
    status,
)
from src import crud
from src.dbmanager import db_manager
from src.dependencies import is_meme_name_available, meme_by_id
from src.models import Meme
from src.private_client import private_client


router = APIRouter(prefix="/memes", tags=["Memes"])


@router.get("/")
async def get_list_memes(
    session=Depends(db_manager.session_dependency),
    page: int = Query(ge=0, default=0),
    size: int = Query(ge=1, le=20, default=1),
):
    memes_list = crud.get_memes(session=session, page=page, size=size)
    return {"memes": memes_list}


@router.get("/{id}/")
async def get_meme_from_id(
    meme: Meme = Depends(meme_by_id),
):
    file_name = meme.file_name
    response = private_client.get_meme_from_id(file_name=file_name)
    return Response(content=response.content, media_type="image/jpeg")


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_meme(
    file_in: UploadFile,
    caption: Annotated[str, Form()],
    session=Depends(db_manager.session_dependency),
):
    is_meme_name_available(session=session, meme_name=file_in.filename)
    response = await private_client.create_meme(file_in=file_in)
    if response.status_code == 201:
        crud.create_meme(
            session=session, file_name=file_in.filename, caption=caption
        )
        return {"message": "Meme created"}


@router.put("/{id}")
async def update_meme(
    file_in: UploadFile,
    caption: Annotated[str, Form()],
    meme: Meme = Depends(meme_by_id),
    session=Depends(db_manager.session_dependency),
):
    old_file_name = meme.file_name
    is_meme_name_available(session=session, meme_name=file_in.filename)
    response = await private_client.update_meme(
        old_file_name=old_file_name, file_in=file_in
    )
    if response.status_code == 201:
        crud.update_meme(
            session=session,
            meme=meme,
            file_name=file_in.filename,
            caption=caption,
        )
        return {"message": "Meme updated"}


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_meme(
    meme: Meme = Depends(meme_by_id),
    session=Depends(db_manager.session_dependency),
):
    response = private_client.delete_meme(file_name=meme.file_name)
    if response.status_code == 204:
        crud.delete_meme(session=session, meme=meme)
        return {"detail": f"Meme {meme.id} was deleted"}
