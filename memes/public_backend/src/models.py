from sqlalchemy import Column, MetaData, SmallInteger, String, Table, Text


metadata = MetaData()


memes = Table(
    "memes",
    metadata,
    Column("meme_id", SmallInteger, primary_key=True),
    Column("file_name", Text, nullable=False),
    Column("caption", String(500), nullable=False),
)
