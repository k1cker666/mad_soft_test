from io import BytesIO

from fastapi import UploadFile
from minio import Minio
from src.settings import Settings, settings


class S3_client:

    s3_client: Minio
    bucket_name: str

    def __init__(self, settings: Settings):
        self.s3_client = Minio(
            endpoint=settings.endpoint,
            access_key=settings.root_user,
            secret_key=settings.root_password,
            secure=False,
        )
        self.bucket_name = settings.bucket_name
        self.__create_bucket()

    def __create_bucket(self):
        bucket = self.s3_client.bucket_exists(self.bucket_name)
        if not bucket:
            self.s3_client.make_bucket(self.bucket_name)

    def get_meme(self, file_name: str) -> BytesIO:
        response = self.s3_client.get_object(
            bucket_name=self.bucket_name, object_name=file_name
        )
        data = BytesIO(response.read())
        response.close()
        response.release_conn()
        return data

    def put_meme(self, file: UploadFile):
        self.s3_client.put_object(
            bucket_name=self.bucket_name,
            object_name=file.filename,
            data=file.file,
            length=file.size,
        )

    def delete_meme(self, file_name: str):
        self.s3_client.remove_object(
            bucket_name=self.bucket_name, object_name=file_name
        )


s3_client = S3_client(settings=settings)
