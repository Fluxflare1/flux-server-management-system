import boto3
from django.conf import settings

def send_metric(metric_name, value, unit='Count'):
    cloudwatch = boto3.client('cloudwatch', region_name=settings.AWS_REGION)
    cloudwatch.put_metric_data(
        Namespace='MyAppMetrics',
        MetricData=[
            {
                'MetricName': metric_name,
                'Value': value,
                'Unit': unit
            },
        ]
    )

def log_error(error_message):
    send_metric('Errors', 1)
    # Additional logging logic
