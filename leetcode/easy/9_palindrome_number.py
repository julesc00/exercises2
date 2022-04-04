class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev_str = str(x)[::-1]
        return str(x) == rev_str


def is_palindrome(x: int) -> bool:
    rev_str = str(x)[::-1]
    rev_int = int(rev_str)
    return x == rev_int


if __name__ == "__main__":
    print(is_palindrome(123))
    print(Solution.isPalindrome(1232))
