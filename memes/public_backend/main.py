import random
from typing import Annotated


from fastapi import FastAPI, Path


app = FastAPI()

@app.get("/memes/")
def get_list_memes():
    return {"memes":"list"}

@app.get("/memes/{id}/")
def get_meme_from_id(id: Annotated[int, Path(ge=1)]):
    memes = ["funny meme", "not funny meme", "best meme", "worst meme"]
    return {
        "meme" : {
            "meme_id" : id,
            "meme" : random.choice(memes)
        }
    }

@app.post("/memes/")
def add_new_meme(meme, caption: str):
    return {"add" : "success"}

@app.put("/memes/{id}")
def update_new_meme(meme):
    return {"update" : "success"}

@app.delete("/memes/{id}")
def delete_new_meme(meme, caption: str):
    return {"delete" : "success"}