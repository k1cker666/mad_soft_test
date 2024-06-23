import os

import pytest
import requests


@pytest.fixture(scope="session")
def post_memes():
    directory = f"{os.path.abspath(os.curdir)}/images/"
    memes = os.listdir(directory)
    memes.sort()
    memes.pop(len(memes) - 1)
    data = {"caption": "Meme caption"}
    for meme in memes:
        with open(directory + meme, "rb") as f:
            file = {"file_in": (meme, f, "image/jpeg")}
            requests.post(
                "http://localhost:8000/memes/", data=data, files=file
            )
