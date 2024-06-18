from fastapi import FastAPI
from src.routers.memes import router as memes_router


app = FastAPI()

app.include_router(memes_router)


@app.get("/")
def main():
    return {
        "detail": "Memes home page",
        "message": "Welcome to memes home page",
    }
