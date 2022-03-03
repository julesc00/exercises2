import pandas_exercises as pd
import numpy as np

my_list = list("abcdefghijklmnopqrstuvwxyz")

my_array = np.arange(26)

my_dict = dict(zip(my_list, my_array))

# Solution
ser1 = pd.Series(my_list)
ser2 = pd.Series(my_array)
ser3 = pd.Series(my_dict)

print(ser3.head())
