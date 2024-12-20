


from django.core.mail import send_mail

def send_email_notification(email, subject, message):
    send_mail(subject, message, "noreply@example.com", [email])

def notify_user(user, title, message):
    # WebSocket Notification
    send_notification(user.id, title, message)

    # Email Notification
    send_email_notification(user.email, title, message)



from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

def send_notification(user_id, title, message):
    channel_layer = get_channel_layer()
    data = {"title": title, "message": message}

    async_to_sync(channel_layer.group_send)(
        f"user_{user_id}",
        {"type": "send_notification", "data": data},
    )



AWS_RATE_CPU_HOUR = 0.1  # Example rate per CPU hour
AWS_RATE_BANDWIDTH_GB = 0.02  # Example rate per GB of bandwidth
PROFIT_MARGIN = 1.10  # 10% profit markup

def calculate_usage_cost(usage):
    cpu_cost = usage.get("cpu_hours", 0) * AWS_RATE_CPU_HOUR
    bandwidth_cost = usage.get("bandwidth_gb", 0) * AWS_RATE_BANDWIDTH_GB
    total_cost = (cpu_cost + bandwidth_cost) * PROFIT_MARGIN
    return total_cost




import boto3

def provision_server(hosting_type, resources):
    ec2 = boto3.client('ec2')

    if hosting_type == "Dedicated":
        instance_type = "t3.2xlarge"  # Example dedicated instance type
    elif hosting_type == "VPS":
        instance_type = "t3.medium"  # Example VPS instance type
    else:  # Shared Hosting
        instance_type = "t3.micro"

    instance = ec2.run_instances(
        InstanceType=instance_type,
        MinCount=1,
        MaxCount=1,
        KeyName="your-ssh-key",
        TagSpecifications=[{
            'ResourceType': 'instance',
            'Tags': [{'Key': 'HostingType', 'Value': hosting_type}]
        }]
    )
    
    return {
        "instance_id": instance['Instances'][0]['InstanceId'],
        "hosting_type": hosting_type,
        "status": "Provisioned"
    }
