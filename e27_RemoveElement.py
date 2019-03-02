class Solution:
    def removeElement(self, nums, val) -> int:
        i = 0
        while True:
            if i >= len(nums):
                break
            if nums[i] == val:
                del nums[i]
                continue
            i += 1
        return len(nums)

nums = [3,2,2,3]
S = Solution()
x = S.removeElement(nums,2)
print(x)