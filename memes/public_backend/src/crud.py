from sqlalchemy import delete, select, update
from sqlalchemy.orm import Session
from src.models import Meme
from src.schemas import MemeOut


def get_memes(session: Session, page: int, size: int) -> list[Meme]:
    offset = page * size
    stmt = select(Meme).order_by(Meme.id).offset(offset).limit(size)
    result = session.execute(stmt)
    meme_list = result.scalars().all()
    meme_name_list = [meme.file_name for meme in meme_list]
    return meme_name_list


def get_meme(session: Session, id: int) -> Meme | None:
    meme = session.query(Meme).filter_by(id=id).one_or_none()
    if meme is None:
        return None
    meme_out = MemeOut(
        id=meme.id, file_name=meme.file_name, caption=meme.caption
    )
    return meme_out


def create_meme(session: Session, file_name: str, caption: str):
    meme = Meme(**{"file_name": file_name, "caption": caption})
    session.add(meme)
    session.commit()
    session.refresh(meme)


def update_meme(session: Session, meme: MemeOut, file_name: str, caption: str):
    stmt = (
        update(Meme)
        .filter_by(id=meme.id)
        .values(file_name=file_name, caption=caption)
    )
    session.execute(stmt)
    session.commit()


def delete_meme(
    session: Session,
    meme: MemeOut,
):
    stmt = delete(Meme).filter_by(id=meme.id)
    session.execute(stmt)
    session.commit()
