from sqlalchemy import select
from sqlalchemy.orm import Session
from src.models import Meme
from src.schemas import MemeCreate


def get_memes(session: Session, offset: int = 0, limit: int = 2) -> list[Meme]:
    stmt = select(Meme).order_by(Meme.id).offset(offset).limit(limit)
    result = session.execute(stmt)
    meme_list = result.scalars().all()
    return meme_list


def get_meme(session: Session, id: int) -> Meme | None:
    meme = session.query(Meme).filter_by(id=id).one_or_none()
    return meme


def create_meme(session: Session, meme_in: MemeCreate) -> Meme:
    meme = Meme(**meme_in.model_dump())
    session.add(meme)
    session.commit()
    session.refresh(meme)
    return meme
