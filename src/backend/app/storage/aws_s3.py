import boto3
from botocore.exceptions import NoCredentialsError

class S3Storage:
    def __init__(self, bucket_name, region_name="us-east-1"):
        self.s3 = boto3.client("s3", region_name=region_name)
        self.bucket_name = bucket_name

    def upload_file(self, file_name, object_name=None):
        try:
            if object_name is None:
                object_name = file_name
            self.s3.upload_file(file_name, self.bucket_name, object_name)
            return f"File uploaded to {self.bucket_name}/{object_name}"
        except NoCredentialsError:
            return "Credentials not available."

    def download_file(self, object_name, file_name):
        try:
            self.s3.download_file(self.bucket_name, object_name, file_name)
            return f"File downloaded to {file_name}"
        except Exception as e:
            return str(e)
