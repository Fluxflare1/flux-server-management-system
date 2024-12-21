import boto3

# Initialize SQS Client
sqs = boto3.client("sqs", region_name="us-east-1")

def send_message(queue_url, message_body):
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=message_body
    )
    return response["MessageId"]

def receive_messages(queue_url, max_messages=10):
    response = sqs.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=max_messages
    )
    return response.get("Messages", [])
