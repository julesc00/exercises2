
"""
Assignment expressions with the walrus operator, since Python3.8
"""

# Classic approach
fh = fopen("filename.txt", "w")
if fh == NULL:

if (fh := fopen("filename.txt", "w")) is None:


"""
With the := operator you can assign and check the result in one operation.
This can be useful when reading user input.
"""
while (line := input("Please enter text: ")) != "":

# The above line can also be expressed:
while line := input("Enter text here: "):

var = 123

