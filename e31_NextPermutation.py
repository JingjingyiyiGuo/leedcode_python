# 我不太明白下一置换的意义，为什么要进行这样的操作？
# 其实这是对于数字全排列的一个顺序的处理
# 问题分析参考：https://blog.csdn.net/xiaoling_000666/article/details/78978120
# Runtime: 44 ms, faster than 98.73% of Python3 online submissions for Next Permutation.
# Memory Usage: 13.1 MB, less than 5.24% of Python3 online submissions for Next Permutation.
class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        :type nums: List[int]
        :rtype: None
        示例：132
        """
        i = len(nums) - 1
        j = len(nums) - 1
        while i > 0 and nums[i] <= nums[i-1]:
            i -= 1
        if i > 0 and nums[i] > nums[i-1]:
            while j >= 0 and nums[j] <= nums[i-1]:   # 编写代码的时候要注意这里的边界值，关注是跟谁比较的
                j -= 1
            if nums[j] > nums[i-1]:  # 编写代码的时候要注意这里的边界值，关注是跟谁比较的
                nums[i-1], nums[j] = nums[j], nums[i-1]
                # nums[i:].sort()   这么写就是错误的，没有进行排序，要注意用法
                nums[i:] = sorted(nums[i:])
        if i == 0:
            nums.sort()

# Runtime: 44 ms, faster than 98.73% of Python3 online submissions for Next Permutation.
# Memory Usage: 13.1 MB, less than 5.24% of Python3 online submissions for Next Permutation.
# class Solution(object):
#     def nextPermutation(self, nums):
#         if len(nums) > 1:  # 如果传入的nums是空的，则什么都不做，否则执行下面的操作
#             for i in range(len(nums) - 1, 0, -1):  # 从数组的末尾考试遍历，因为存在i-1，所以0不遍历
#                 if nums[i - 1] < nums[i]:  # 如果到i-1的时候发现不是递增序列
#                     for j in range(len(nums) - 1, i - 1, -1):  # 倒着遍历，一直到第i个元素位置
#                         if nums[j] > nums[i - 1]:  # 寻找第一个比i-1大的元素
#                             nums[i - 1], nums[j] = nums[j], nums[i - 1]   # 找到了以后交换
#                             nums[i:] = sorted(nums[i:])  # 对从i往后的元素排序【注意这里是正序】
#                             break  # 完成了交换使命，跳出循环
#                     break  # 完成了交换使命，跳出循环
#                 if i == 1:  # 如果一直表里到了头，都没找到非递增值，则说明当前排序为逆序，直接按照正序排序即可
#                     nums.sort()

# nums = [-1, 0, 1, 2, -1, -4]
nums = [1,3,2]
S = Solution()
S.nextPermutation(nums)
print(nums)