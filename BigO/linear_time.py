"""
Linear time algorithms mean that every single element from the input is visited exactly once,
O(n) times. As the size of the input, N, grows our algorithm’s run time scales exactly with
the size of the input.

Linear running time algorithms are widespread. Linear runtime means that the program visits
every element from the input. Linear time complexity O(n) means that as the input grows,
the algorithms take proportionally longer to complete.2 Apr 2019
"""
shopping_list = ["Bread", "Butter", "The Nacho Libre soundtrack from the 2006 film Nacho Libre",
                 "Reusable Water Bottle"]

[print(item) for item in shopping_list]
