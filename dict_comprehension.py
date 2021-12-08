from collections import OrderedDict, defaultdict

users = [
    (0, "Bob", "password"),
    (1, "Benito", "beni123"),
    (2, "Jemima", "jemi321"),
    (3, "Charbel", "chulito123")
]

users2 = [
    ("Caricia", "Briones", "cari@changuis.com"),
    ("Franzche", "Briones", "punky@changuis.com"),
    ("Brigitte", "Briones", "gigitte@changuis.com"),
    ("Michele", "Briones", "chenis@changuis.com"),
    ("Jemima", "Briones", "jemi@changuis.com"),
]

users_dict = {}
for user in users2:
    users_dict["first_name"] = user[0]
    users_dict["last_name"] = user[1]
    users_dict["email"] = user[2]

print(users_dict)

username_mapping = {user[1]: user for user in users}

# prints: {'Bob': (0, 'Bob', 'password'), 'Benito': (1, 'Benito', 'beni123'), 'Jemima': (2, 'Jemima', 'jemi321'), \
# 'Charbel': (3, 'Charbel', 'chulito123')}
print(username_mapping)

# Gets: (2, 'Jemima', 'jemi321')
print(username_mapping.get("Jemima"))

# Example of usage
username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

_, username, password = username_mapping[username_input]

if password_input == password:
    print("Your details are correct!")
else:
    print("Your details are incorrect!")
