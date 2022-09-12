import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("hot_update_parameters")
print(table.creation_date_time)


def create_item():
    table.put_item(
        Item={
            "current": "0",
            "accepted_update_version_index": 0,
            "backup_in_progress_index": 0,
            "cancel_deployment_index": "False",
            "deploy_in_progress_index": 0,
            "refresh_in_progress_index": 0,
            "restore_in_progress_index": 0
        }
    )


def create_items():
    for num in range(3):
        table.put_item(Item={
            "id": num,
            "name": f"Julito{num}"
        })


def get_item():
    response = table.get_item(
        Key={
            "username": "julito",
            "last_name": "Briones Huerta"
        }
    )
    item = response.get("Item")
    print(item)


def update_item():
    response = table.update_item(
        Key={
            "username": "julito",
            "last_name": "Briones Huerta"
        },
        UpdateExpression="SET age = :val1",
        ExpressionAttributeValues={":val1": 26}
    )


def delete_item():
    table.delete_item(
        Key={
            "username": "julito",
            "last_name": "Briones Huerta"
        }
    )
