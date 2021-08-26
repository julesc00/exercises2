"""
Parameters :
obj : The object whose which attribute has to be checked.
key : Attribute which needs to be checked.

Returns : Returns True, if attribute is present else returns False.
"""


class GFC:
    name = "GeekforGeeks"
    age = 24


# initializing object
obj = GFC()

# using hasattr() to check name
print(f"Does name exists? {str(hasattr(obj, 'name'))}")

# using hasattr() to check motto
print(f"Does motto exist? {str(hasattr(obj, 'motto'))}")


