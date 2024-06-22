from sqlalchemy import select
from sqlalchemy.orm import Session
from src.models import Meme


def get_memes(session: Session, page: int, size: int) -> list[Meme]:
    offset = page * size
    stmt = select(Meme).order_by(Meme.id).offset(offset).limit(size)
    result = session.execute(stmt)
    meme_list = result.scalars().all()
    meme_name_list = [meme.__dict__ for meme in meme_list]
    return meme_name_list


def get_meme(session: Session, id: int) -> Meme | None:
    meme = session.query(Meme).filter_by(id=id).one_or_none()
    return meme


def create_meme(session: Session, file_name: str, caption: str):
    meme = Meme(**{"file_name": file_name, "caption": caption})
    session.add(meme)
    session.commit()
    session.refresh(meme)


def update_meme(session: Session, meme: Meme, file_name: str, caption: str):
    meme.file_name = file_name
    meme.caption = caption
    session.commit()


def delete_meme(
    session: Session,
    meme: Meme,
):
    session.delete(meme)
    session.commit()
