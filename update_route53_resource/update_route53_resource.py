import boto3

def lambda_handler(event, context):
    route53 = boto3.client("route53")

    hosted_zone_id = event["hosted_zone_id"]
    record_type = event["record_type"]
    record = event["record"]
    new_record_value = event["new_record_value"]

    dns_change = {
        "Changes": [
            {
                "Action": "UPSERT",
                "ResourceRecordSet": {
                    "Name": record,
                    "Type": record_type,
                    "TTL": 300,
                    "ResourceRecords": [
                        {
                            "Value": new_record_value
                        }
                    ]
                }
            }
        ]
    }

    response = route53.change_resource_record_sets(HostedZoneId = hosted_zone_id, ChangeBatch = dns_change)

    return {"status":response["ChangeInfo"]["Status"]}