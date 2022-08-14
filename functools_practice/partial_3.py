from functools import partial
import math
import statistics
from typing import List, Set

"""
Partial functions are derived functions that have some pre-assigned input 
parameters. For example, if a function takes in two parameters say “a” and “b”, 
a partial function can be created from it that has “a” as a prefilled argument 
and it can then be called with “b” as the only parameter. 
Functool’s partial() is used to create partial functions/objects and this is a 
useful feature as it allows for the:

    1. Replication of existing functions with some arguments already passed in.
    2. Creation of newer version of the existing function in a well-documented 
        manner.
"""

