import os
import psycopg
from settings import settings

class Migration:

    connection: psycopg.Connection

    def __init__(self, conninfo: str):
        self.connection = psycopg.connect(
            conninfo=conninfo
        )

    def create_table(self):
        with self.connection.cursor() as curs:
            stmt = (
                """create table if not exists memes (
                id smallserial primary key,
                file_name varchar(20) not null,
                caption varchar(500) not null
                );"""
            )
            curs.execute(stmt)
        self.connection.commit()

    def insert_memes(self):
        directory = f"{os.path.abspath(os.curdir)}/memes/images/"
        files = os.listdir(directory)
        with self.connection.cursor() as curs:
            for file_ in files:
                file_ = "test"
                curs.execute("insert into memes (file_name, caption) values (%s, 'example');", (file_,))
        self.connection.commit()


if __name__ == "__main__":
    db = Migration(settings.conninfo)
    db.create_table()
    db.insert_memes()