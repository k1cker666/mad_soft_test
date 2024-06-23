import os

import requests


def test_get_memes(post_memes):
    post_memes
    response = requests.get(
        "http://localhost:8000/memes/", params={"size": "4"}
    )
    assert response.status_code == 200
    assert len(response.json()["memes"]) == 4


def test_get_meme_by_id():
    response = requests.get("http://localhost:8000/memes/1/")
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/jpeg"


def test_update_meme():
    directory = f"{os.path.abspath(os.curdir)}/images/"
    meme = "meme_5.jpg"
    data = {"caption": "Meme caption"}
    with open(directory + meme, "rb") as f:
        file = {"file_in": (meme, f, "image/jpeg")}
        response = requests.put(
            "http://localhost:8000/memes/4", data=data, files=file
        )
    assert response.status_code == 200
    assert response.json() == {"message": "Meme updated"}


def test_delete_meme():
    response = requests.delete("http://localhost:8000/memes/5")
    assert response.status_code == 204


def test_delete_meme_none():
    response = requests.delete("http://localhost:8000/memes/10")
    assert response.status_code == 404
