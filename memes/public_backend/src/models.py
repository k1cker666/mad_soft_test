from sqlalchemy import Column, MetaData, SmallInteger, String, Table, Text


metadata = MetaData()


memes = Table(
    "memes",
    metadata,
    Column("meme_id", SmallInteger, primary_key=True),
    Column("image", Text, nullable=False),
    Column("caption", String, nullable=False),
)
