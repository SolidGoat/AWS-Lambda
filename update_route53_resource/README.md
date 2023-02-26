# Update AWS Route53 Resource Record

AWS Lambda that updates Route53 resource record. If it doesn't exist, it will create it.

## Input

```json
{
    "hosted_zone_id": "Z3P5QSUBK4POTI",
    "record_type": "CNAME",
    "record": "www2.example.com",
    "new_record_value": "d111111abcdef8.cloudfront.net"
}

```