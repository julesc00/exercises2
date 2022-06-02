"""
Encapsulation hides the data from the outer world. In Python, we can hide the variable and method by using the
underscore symbol, which are double "_" and "__" double.
"""


class UserAuthentication:
    # We define the constructor
    # Calling __userAuth(), because we can call only inside the class.
    def __init__(self):
        self.__userAuth()

    def action_page(self):
        print("User authentication is completed.")

    # Definition of __userAuth method.
    # It's access scope is only inside the class
    def __userAuth(self):
        print("User validation process is going on...")


user_obj = UserAuthentication()
print(user_obj.action_page())
