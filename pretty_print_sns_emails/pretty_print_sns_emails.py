import boto3
import json
import os

client = boto3.client('sns')

# Create 'topic_arn' environment variable and set it to your SNS topic's arn
# arn:aws:sns:<region>:<account_id>:<topic_name>
topic_arn = os.environ['topic_arn']

def lambda_handler(event, context):
    message = json.dumps(event, indent=4, sort_keys=False)
    response = client.publish(TopicArn=topic_arn, Message=message)
    
    return response