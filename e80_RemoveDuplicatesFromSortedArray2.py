# Runtime: 52 ms, faster than 63.86% of Python3 online submissions for Remove Duplicates from Sorted Array II.
# Memory Usage: 13.2 MB, less than 5.43% of Python3 online submissions for Remove Duplicates from Sorted Array II.
# 时间复杂度O(n)，空间复杂度O(1)
class Solution:
    def removeDuplicates(self, nums) -> int:
        if len(nums) < 1:
            return 0
        i = 0
        r = 0
        for j in range(1, len(nums)):
            if nums[j] == nums[i]:
                r += 1
                if r < 2:
                    i += 1
                    nums[i] = nums[j]
            else:
                i += 1
                nums[i] = nums[j]
                r = 0
        return i + 1
