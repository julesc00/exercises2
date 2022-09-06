import boto3


def lambda_handler(event, context):
    db = boto3.resource("dynamodb")
    response = db.batch_get_item(
        RequestedItems={
            "Users": {
                "Keys": [
                    {
                        "id": 1
                    },
                    {
                        "id": 2
                    }
                ]
            }
        }
    )