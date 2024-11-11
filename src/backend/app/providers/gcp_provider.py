from googleapiclient.discovery import build
from google.oauth2 import service_account
from config.logging_config import log_error

class GCPProvider:
    def __init__(self):
        credentials = service_account.Credentials.from_service_account_file("path/to/credentials.json")
        self.compute = build("compute", "v1", credentials=credentials)

    def start_instance(self, instance_name, zone):
        try:
            response = self.compute.instances().start(project="project_id", zone=zone, instance=instance_name).execute()
            return response
        except Exception as e:
            log_error(f"GCP Start Instance Error: {e}")
            raise e
