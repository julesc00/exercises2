

class Solution:
    def __init__(self, coins=[]):
        self.coins = coins

    def first_attempt(self):
        coins = sorted(self.coins)

        constructible_change = 0
        for coin in coins:
            if coin > constructible_change + 2:
                break
            constructible_change += 1
        return constructible_change + 1

    def second_attempt(self):
        pass


if __name__ == "__main__":
    coins = [1, 2, 5]
    # coins = []
    solution = Solution(coins)

    print(solution.first_attempt())
    print(solution.second_attempt())
