from google.cloud import storage

class GCSStorage:
    def __init__(self, bucket_name):
        self.client = storage.Client()
        self.bucket = self.client.bucket(bucket_name)

    def upload_file(self, file_path, blob_name):
        blob = self.bucket.blob(blob_name)
        blob.upload_from_filename(file_path)
        return f"File uploaded to {self.bucket.name}/{blob_name}"

    def download_file(self, blob_name, destination_file_path):
        blob = self.bucket.blob(blob_name)
        blob.download_to_filename(destination_file_path)
        return f"File downloaded to {destination_file_path}"
