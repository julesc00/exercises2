"""
setattr() is used to assign the object attribute its value.
Apart from ways to assign values to class variables, through
constructors and object functions, this method gives you an
alternative way to assign value.

Syntax : setattr(obj, var, val)

Parameters :
obj : Object whose which attribute is to be assigned.
var : object attribute which has to be assigned.
val : value with which variable is to be assigned.

Returns :
None
"""


class Gfg:
    name = "GeeksforGeeks"


# initializing object
obj = Gfg()

print(f"Before setattr name: {obj.name}")

# using setattr to change name
setattr(obj, "name", "Geeks4Geeks")

print(f"After setattr name: {obj.name}")
