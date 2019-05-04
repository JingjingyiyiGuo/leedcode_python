# 暴力解法：
# 超时
class Solution:
    def removeDuplicates(self, nums) -> int:
        for i in range(len(nums)):
            if nums[i] == 'a':
                continue
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    nums[j] = 'a'
        k = 0
        while True:
            if k >= len(nums):
                break
            if nums[k] == 'a':
                del nums[k]
                continue
            k += 1
        return len(nums)

# Runtime: 56 ms, faster than 95.51% of Python3 online submissions for Remove Duplicates from Sorted Array.
# Memory Usage: 14.8 MB, less than 5.43% of Python3 online submissions for Remove Duplicates from Sorted Array.
# 时间复杂度O(n^2)，空间复杂度O(1)
class Solution:
    def removeDuplicates(self, nums) -> int:
        if len(nums) < 1:
            return 0
        i = 0
        for j in range(1,len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1

# 可以用二分查找，思考一下


nums = [0,0,1,1,1,2,2,3,3,4]
S = Solution()
x = S.removeDuplicates(nums)
print(x)