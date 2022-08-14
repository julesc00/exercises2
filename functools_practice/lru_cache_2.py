from functools import lru_cache

"""
lru_cache() is a decorator, which wraps a function with a memoizing callable 
used for saving up to maxsize the results of a function call and returns the 
stored value if the function is called with the same arguments again. It can 
save time when an expensive or I/O bound function is periodically called with 
the same arguments.

Essentially it uses two data structures, a dictionary to map a function’s 
parameters to its result, and a linked list to keep track of the function’s 
call history.

In full LRU Cache stands for Least-Recently-Used Cache and refers to a cache 
which drops the least recently used element if the maximum size of entries is 
reached. The LRU feature is disabled if maxsize is set to None and caches 
arguments of different data types separately if typed is True e.g., 
f(3) and f(3.0) will be cached distinctly.

An example of the utility of lru_cache() can be shown in optimizing code 
that generates the factorial of a number.

NOTE:   In general, the LRU cache should only be used when you want to reuse 
        previously computed values. Accordingly, it doesn’t make sense to cache 
        functions that need to create distinct mutable objects on each call. 
        Also, since a dictionary is used to cache results, the positional 
        and keyword arguments to the function must be hashable.
"""


# Function without lru_cache
def uncached_factorial(n):
    if n <= 1:
        return 1
    return n * uncached_factorial(n-1)


@lru_cache(maxsize=None)
def cached_factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n * uncached_factorial(n-1)
