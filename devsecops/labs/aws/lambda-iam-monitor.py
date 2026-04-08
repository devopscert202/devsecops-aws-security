"""
AWS Lambda — IAM Access Key Creation Monitor

Triggered by EventBridge when CreateAccessKey API is called.
Records the event in a DynamoDB table for audit purposes.

Environment:
    TABLE_NAME: DynamoDB table name (default: iamkey_storer)
    REGION: AWS region (default: us-east-1)
"""
import json
import os
from datetime import datetime

import boto3

TABLE_NAME = os.environ.get("TABLE_NAME", "iamkey_storer")
REGION = os.environ.get("REGION", "us-east-1")

dynamodb = boto3.resource("dynamodb", region_name=REGION)
table = dynamodb.Table(TABLE_NAME)


def lambda_handler(event, context):
    """Process CreateAccessKey CloudTrail event and store in DynamoDB."""
    print(json.dumps(event, default=str))

    detail = event.get("detail", {})
    response_elements = detail.get("responseElements", {})
    access_key_info = response_elements.get("accessKey", {})

    creation_time_str = access_key_info.get("createDate", "")
    try:
        creation_time = datetime.strptime(
            creation_time_str, "%b %d, %Y %I:%M:%S %p"
        )
        created_on = creation_time.strftime("%Y-%m-%dT%H:%M:%SZ")
    except (ValueError, TypeError):
        created_on = creation_time_str

    item = {
        "cloudtrail_key": event.get("id", "unknown"),
        "access_key": access_key_info.get("accessKeyId", "unknown"),
        "created_on": created_on,
        "sourceIPAddress": detail.get("sourceIPAddress", "unknown"),
        "userName": detail.get("userIdentity", {}).get("userName", "unknown"),
    }

    table.put_item(Item=item)

    return {"statusCode": 200, "body": json.dumps("Event recorded successfully")}
