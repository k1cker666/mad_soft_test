from fastapi import FastAPI, UploadFile
from fastapi.responses import StreamingResponse
from src.s3_client import s3_client


app = FastAPI()


@app.get("/get_meme/{file_name}")
async def get_meme(file_name: str):
    data = s3_client.get_meme(file_name=file_name)
    return StreamingResponse(content=data, media_type="image/jpeg")


@app.post("/post_meme/")
async def put_meme(file: UploadFile):
    s3_client.put_meme(file=file)


@app.delete("/delete_meme/{file_name}")
async def delete_meme(file_name: str):
    s3_client.delete_meme(file_name=file_name)
