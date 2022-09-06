import boto3


def lambda_handler(event, context):
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.create_table(
        TableName="users",
        KeySchema=[
            {
                "AttributeName": "id",
                "KeyType": "HASH"
            },
            {
                "AttributeName": "name",
                "KeyType": "RANGE"
            }
        ],
        AttributeDefinitions=[
            {
                "AttributeName": "id",
                "AttributeType": "N"
            },
            {
                "AttributeName": "name",
                "AttributeType": "S"
            }
        ],
        ProvisionedThroughput={
            "ReadCapacityUnits": 5,
            "WriteCapacityUnits": 5
        }
    )

    table.wait_until_exists()
    print(f"Table count: {table.table_count}")
    print(f"Print table status: {table.table_status}")
