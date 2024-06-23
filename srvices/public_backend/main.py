from fastapi import FastAPI
from src.routers.memes import router as memes_router


app = FastAPI()

app.include_router(memes_router)


@app.get("/ping/")
async def ping():
    return {"message": "pong"}
