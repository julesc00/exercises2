import boto3


def lambda_handler(event, context):
    db = boto3.resource("dynamodb")
    table = db.Table("users")
    with table.batch_writer() as batch:
        batch.put_item(
            Item={
                "id": 1,
                "name": "Julito",
                "age": "16"
            },
        )
        batch.put_item(
            Item={
                "id": 2,
                "name": "Jemima",
                "age": "1"
            },
        )
        batch.put_item(
            Item={
                "id": 3,
                "name": "Jules",
                "age": "19"
            },
        )

    table.put_item(
        Item={
            "id": 1,
            "name": "Charbelito"
        }
    )
