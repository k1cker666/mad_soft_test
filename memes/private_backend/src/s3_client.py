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


s3_client = S3_client(settings=settings)
