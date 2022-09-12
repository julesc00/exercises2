import json


def lambda_handler(event, context):
    print("--------------------------")
    try:
        for record in event["Records"]:
            if record["eventName"] == "INSERT":
                handle_insert(record)
            elif record["eventName"] == "MODIFY":
                handle_modify(record)
            elif record["eventName"] == "REMOVE":
                handle_remove(record)
        print("--------------------------")
    except Exception as e:
        print(e)
        print("--------------------------")
        return "Oops!"


def handle_insert(record):
    print("Handling INSERT event")

    # 3a Get newImage content
    new_image = record["dynamodb"]["NewImage"]

    # 3b Parse the values
    new_player_id = new_image["playerId"]["S"]

    # 3c Print it out
    print("New row added with playerId=" + new_player_id)
    print("Done handling INSERT event")


def handle_modify(record):
    # 3a Parse oldImage and score
    old_image = record["dynamodb"]["OldImage"]
    old_score = old_image["score"]["N"]

    # 3b Parse oldImage and score
    new_image = record["dynamodb"]["NewImage"]
    new_score = new_image["score"]["N"]

    # 3c Check for change
    if old_score != new_score:
        print(f"Scores changed - oldScore={old_score}, newScore={new_score}")
    print("Done handling MODIFY event")


def handle_remove(record):
    print("Handling REMOVE event")

    # 3a Parse oldImage
    old_image = record["dynamodb"]["OldImage"]

    # 3b Parse the values
    old_player_id = old_image["playerId"]["S"]

    # 3c Print it out
    print(f"Row removed with playerId={old_player_id}")

    print("Done REMOVE event")
