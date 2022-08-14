from functools import reduce

"""
First up we have a classic. The reduce(function, sequence) function receives 
two arguments, a function and an iterable. It applies the argument function 
cumulatively to all elements of the iterable from the left to the right and 
then returns a single value.

To put it simply, it first applies the argument function to the first two 
elements of the iterable and the value returned by this first call becomes 
the function’s first argument and the third element of the iterable becomes 
the second argument. This process is repeated until the iterable is exhausted.

For example, reduce() can be used to easily calculate the sum or the product 
of a list.
"""

lst1 = [1, 2, 3, 4]
lst2 = [i for i in range(11)]
print(lst2)
list_sum = reduce(lambda x, y: x+y, lst1)
list_sum2 = reduce(lambda x, y: x+y, lst2)
list_product = reduce(lambda x, y: x*y, lst1)
print(list_sum)
print(list_sum2)
print(list_product)
