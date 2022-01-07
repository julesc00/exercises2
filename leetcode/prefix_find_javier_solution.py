
class Solution:

    def longest_common_prefix(self, strs: list[str]) -> str:
        result = []
        for characters in zip(*strs):
            equal = True
            for i in range(1, len(characters)):
                # print(characters[i], characters[i - 1])
                if characters[i] != characters[i - 1]:
                    equal = False
                    break
            if equal:
                result.append(characters[0])
            else:
                break
        return ''.join(result)


if __name__ == "__main__":
    strings = ["primary", "prix", "practice", "print", "prior", "aaaa"]
    sol = Solution()
    print(sol.longest_common_prefix(strings))
