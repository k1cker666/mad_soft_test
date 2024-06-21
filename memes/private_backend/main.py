from io import BytesIO

from fastapi import FastAPI
from src.s3_client import s3_client


app = FastAPI()


@app.get("/meme/{file_name}")
def get_meme(file_name: str):
    meme = s3_client.get_meme(file_name=file_name)
    return meme


@app.post("/meme/{file_name}")
def put_meme(file_name: str, data: BytesIO):
    s3_client.put_meme(file_name=file_name, data=data)
