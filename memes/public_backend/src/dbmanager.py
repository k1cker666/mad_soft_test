from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.settings import settings


class DBManager:
    def __init__(self, conninfo: str, echo: bool):
        self.engine = create_engine(
            url=conninfo,
            echo=echo,
        )
        self.session_factory = sessionmaker(
            bind=self.engine,
            autoflush=False,
            expire_on_commit=False,
        )

    def session_dependency(self):
        with self.session_factory() as session:
            yield session
            session.close()


db_manager = DBManager(
    conninfo=settings.conninfo,
    echo=settings.echo,
)
