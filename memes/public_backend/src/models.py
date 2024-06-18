from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True)


class Meme(Base):
    __tablename__ = "memes"

    file_name: Mapped[str] = mapped_column(String(20))
    caption: Mapped[str] = mapped_column(String(500))
