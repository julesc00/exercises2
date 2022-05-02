import requests
from pprint import PrettyPrinter
from collections import defaultdict, OrderedDict, namedtuple


USERS_URL = "https://www.scalablepath.com/api/test/test-users"
POSTS_URL = "https://www.scalablepath.com/api/test/test-posts"

pp = PrettyPrinter(indent=3, depth=3)


def json_to_dict():

    try:
        users_res = requests.get(USERS_URL).json()
        posts_res = requests.get(POSTS_URL).json()
        users = [(u["name"], u["id"]) for u in users_res]
        posts = [(p["userId"], p["title"], p["body"]) for p in posts_res]
        posts_lst, counter = [], len(users_res)
        temp_dict, temp_dict2 = {}, {}
        while counter:
            for user in users:

                temp_dict.update({
                    "name": user[0],
                    "id": user[1],
                    "posts": []
                })
                posts_lst.append(temp_dict)
                counter -= 1

        counter = len(posts_res)
        while counter:
            for post in posts:
                if post[0] == posts_lst[0]["id"]:
                    temp_dict2.update({
                        "title": post[1],
                        "body": post[2]
                    })
                    temp_dict["posts"].append(temp_dict2)
                    counter -= 1

        print(users)
        print(posts)
        pp.pprint(posts_lst)
    except ConnectionError:
        print("whatever")


if __name__ == "__main__":
    json_to_dict()
