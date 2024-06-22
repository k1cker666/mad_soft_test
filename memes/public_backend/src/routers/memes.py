from typing import Annotated

import requests
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


router = APIRouter(prefix="/memes", tags=["Memes"])


@router.get("/")
def get_list_memes(
    session=Depends(db_manager.session_dependency),
    page: int = Query(ge=0, le=5, default=0),
    size: int = Query(ge=1, le=5, default=1),
):
    memes_list = crud.get_memes(session=session, page=page, size=size)
    return {"meme_name_list": memes_list}


@router.get("/{id}/")
async def get_meme_from_id(
    meme: Meme = Depends(meme_by_id),
):
    file_name = meme.file_name
    response = requests.get(f"http://localhost:8020/get_meme/{file_name}")
    return Response(content=response.content, media_type="image/jpeg")


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_meme(
    file: UploadFile,
    caption: Annotated[str, Form()],
    session=Depends(db_manager.session_dependency),
):
    is_meme_name_available(session=session, meme_name=file.filename)
    crud.create_meme(session=session, file_name=file.filename, caption=caption)
    file_content = await file.read()
    files = {"file": (file.filename, file_content, file.content_type)}
    response = requests.post(
        url="http://localhost:8020/post_meme/", files=files
    )
    if response.status_code == 200:
        return {"message": "Meme created"}
    return {"message": "Meme created"}


@router.put("/{id}")
def update_meme(
    file: UploadFile,
    caption: Annotated[str, Form()],
    meme: Meme = Depends(meme_by_id),
    session=Depends(db_manager.session_dependency),
):
    is_meme_name_available(session=session, meme_name=file.filename)
    crud.update_meme(
        session=session,
        meme=meme,
        file_name=file.filename,
        caption=caption,
    )
    return {"message": "Meme updated"}


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_meme(
    meme: Meme = Depends(meme_by_id),
    session=Depends(db_manager.session_dependency),
):
    crud.delete_meme(session=session, meme=meme)
    return {"detail": f"Meme {meme.id} was deleted"}
