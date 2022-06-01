
class Solution:

    def sort_array_by_parity(self, nums):
        insert_idx = 0
        for pos in range(len(nums))[::-1]:
            if insert_idx >= pos:
                return nums
            while nums[pos] % 2 == 0:
                v = nums.pop(pos)
                nums.insert(0, v)
                insert_idx += 1
                if insert_idx >= pos:
                    break
