import requests
from fastapi import UploadFile


class PrivateClient:

    base_url = "http://private_api:8002"

    def get_meme_from_id(
        self,
        file_name: str,
    ) -> requests.Response:
        response = requests.get(f"{self.base_url}/get_meme/{file_name}")
        return response

    async def create_meme(
        self,
        file_in: UploadFile,
    ) -> requests.Response:
        file_content = await file_in.read()
        file = {"file": (file_in.filename, file_content, file_in.content_type)}
        response = requests.post(url=f"{self.base_url}/post_meme/", files=file)
        return response

    async def update_meme(
        self,
        old_file_name: str,
        file_in: UploadFile,
    ) -> requests.Response:
        requests.delete(url=f"{self.base_url}/delete_meme/{old_file_name}")
        file_content = await file_in.read()
        file = {"file": (file_in.filename, file_content, file_in.content_type)}
        response = requests.post(url=f"{self.base_url}/post_meme/", files=file)
        return response

    def delete_meme(
        self,
        file_name: str,
    ) -> requests.Response:
        response = requests.delete(
            url=f"{self.base_url}/delete_meme/{file_name}"
        )
        return response


private_client = PrivateClient()
