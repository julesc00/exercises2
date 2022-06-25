import json
import boto3

client = boto3.client("event")


def lambda_handler(event, context):
    print(event)
    response = client.put_events(
        Entries=[
            {
                "source": "Producer",
                "DetailType": "Lambda function producer",
                "Detail": json.dumps({
                    "Key": "Value"
                }),
            },
        ]
    )

    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
