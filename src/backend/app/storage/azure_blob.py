from azure.storage.blob import BlobServiceClient

class AzureBlobStorage:
    def __init__(self, connection_string, container_name):
        self.service_client = BlobServiceClient.from_connection_string(connection_string)
        self.container_client = self.service_client.get_container_client(container_name)

    def upload_file(self, file_path, blob_name):
        with open(file_path, "rb") as data:
            self.container_client.upload_blob(name=blob_name, data=data, overwrite=True)
        return f"File uploaded to {blob_name}"

    def download_file(self, blob_name, destination_file_path):
        with open(destination_file_path, "wb") as file:
            blob_client = self.container_client.get_blob_client(blob_name)
            file.write(blob_client.download_blob().readall())
        return f"File downloaded to {destination_file_path}"
