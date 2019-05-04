# Runtime: 48 ms, faster than 64.08% of Python3 online submissions for Maximum Subarray.
# Memory Usage: 13.6 MB, less than 5.50% of Python3 online submissions for Maximum Subarray.
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        pre = nums[0]
        for i in range(1, len(nums)):
            current = max(pre + nums[i], nums[i])
            pre  = current
            max_sum = max(max_sum, current)
        return max_sum