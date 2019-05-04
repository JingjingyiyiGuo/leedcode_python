# Runtime: 48 ms, faster than 64.08% of Python3 online submissions for Maximum Subarray.
# Memory Usage: 13.6 MB, less than 5.50% of Python3 online submissions for Maximum Subarray.
# 时间复杂度O(n)，空间复杂度O(1)。
# 用了动态规划的方法，DP方程控制的是以当前位置为子序列结尾处的子序列的最大和。
class Solution:
    def maxSubArray(self, nums) -> int:
        max_sum = nums[0]
        pre = nums[0]
        for i in range(1, len(nums)):
            current = max(pre + nums[i], nums[i])
            pre = current
            max_sum = max(max_sum, current)
        return max_sum

# leedcode上超时了
# 时间复杂度O(n^2)，空间复杂度O(n)。
class Solution:
    def maxSubArray(self, nums) -> int:
        sum_arr = []
        sum_arr.append(0)
        for i in range(1,len(nums)+1):
            sum_arr.append(sum_arr[-1] + nums[i-1])  # 考虑边界值问题
        max_sum = nums[0]   # 用到的要检查是否赋值了
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                current = sum_arr[j+1] - sum_arr[i]  # 一定要考虑到边界值问题，手写完成后多检查几遍
                max_sum = max(current, max_sum)
        return max_sum