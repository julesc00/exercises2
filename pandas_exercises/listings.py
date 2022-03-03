import pandas as pd

account_info = pd.DataFrame({
    "name": ["Jemima", "Michele", "Jules"],
    "account": [12345, 42334, 22321],
    "balance": [12323, 34323, 33554]
})

# account_info["name"] = ["Cesar", "Punky", "Tai"]
# print(account_info)
# print(account_info[["name", "balance"]])


"""
The iloc method
A DataFrame’s rows can be accessed via the iloc method which uses a list-like syntax.
    Example: account_info.iloc[1]
        name       Michele
        account      42334
        balance      34323
        Name: 1, dtype: object
"""
print(account_info.iloc[1])
print(account_info.iloc[0:2])
