
"""
It is the concept where we write the class more than once. In that case, one method overwrites the other that is
depending upon the calling sequence.
"""


# Class for printing string messages on the console.
class StrMsg:

    def show_msg(self):
        print("show_msg() method for class StrMsg")


# Class for printing Integer value on the console.
class IntMsg(StrMsg):
    def show_msg(self):
        print("show_msg() method from class IntMsg")


int_msg_obj = IntMsg()
str_msg_obj = StrMsg()
print(int_msg_obj.show_msg())
print(str_msg_obj.show_msg())
