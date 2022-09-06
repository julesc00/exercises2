import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("users")
print(table.creation_date_time)


def create_item():
    table.put_item(
        Item={
            "username": "julito",
            "first_name": "Julio",
            "last_name": "Briones Huerta",
            "age": 25,
            "account_type": "standard_user"
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
