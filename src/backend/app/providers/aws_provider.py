from config.logging_config import log_error
import boto3
from botocore.exceptions import ClientError

class AWSProvider:
    def __init__(self):
        self.client = boto3.client("ec2")

    def start_instance(self, instance_id):
        try:
            response = self.client.start_instances(InstanceIds=[instance_id])
            return response
        except ClientError as e:
            log_error(f"AWS Start Instance Error: {e}")
            raise e
