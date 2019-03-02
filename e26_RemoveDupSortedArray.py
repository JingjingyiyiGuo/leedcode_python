# 暴力解法：
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



nums = [0,0,1,1,1,2,2,3,3,4]
S = Solution()
x = S.removeDuplicates(nums)
print(x)