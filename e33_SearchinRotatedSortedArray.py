class Solution:
    def search(self, nums, target) -> int:
        real_medi = len(nums) // 2
        start = 0
        end = len(nums)
        while start < end:
            medi = (end - start) // 2 + start
            if target == nums[medi]:
                return medi
            elif target < nums[medi]:
                end = medi
            else:
                start = medi + 1
        if start <= real_medi:
            start = real_medi + 1
            end = len(nums)
        else:
            start = 0
            end = real_medi
        while start < end:
            medi = (end - start) // 2 + start
            if target == nums[medi]:
                return medi
            elif target < nums[medi]:
                end = medi
            else:
                start = medi + 1
        return -1


nums = [4,5,6,7,0,1,2]
target = 0
S = Solution()
x = S.search(nums, target)
print(x)

nums = [4,5,6,7,0,1,2]
target = 3
S = Solution()
x = S.search(nums, target)
print(x)