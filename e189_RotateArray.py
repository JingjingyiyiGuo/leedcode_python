# Runtime: 72 ms, faster than 28.94% of Python3 online submissions for Rotate Array.
# Memory Usage: 13.5 MB, less than 5.04% of Python3 online submissions for Rotate Array.
# 时间复杂度O(n)，空间复杂度O(n)。
# class Solution:
#     def rotate(self, nums, k) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         new = [0 for i in range(len(nums))]
#         for i in range(len(nums)):
#             new[(i+k)%len(nums)] = nums[i]
#         for i in range(len(nums)):
#             nums[i] = new[i]

# 超时
# 时间复杂度O(n^2)，空间复杂度O(1)。
# class Solution:
#     def rotate(self, nums, k) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         for i in range(k):
#             previous = nums[len(nums)-1]
#             for j in range(len(nums)):
#                 temp = nums[j]
#                 nums[j] = previous
#                 previous = temp

# Runtime: 56 ms, faster than 59.04% of Python3 online submissions for Rotate Array.
# Memory Usage: 13.6 MB, less than 5.04% of Python3 online submissions for Rotate Array.
# 时间复杂度O(n)，空间复杂度O(1)。
# 这里使用了远距离交换的思想，类比希尔排序的思想。
# class Solution:
#     def rotate(self, nums, k) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         k = k % len(nums)
#         start = 0
#         count = 0
#         while count < len(nums):
#             current = start
#             prev = nums[start]
#             while True:
#                 next1 = (current + k) % len(nums)
#                 temp = nums[next1]
#                 nums[next1] = prev
#                 prev = temp
#                 current = next1
#                 count += 1
#                 if start == current:
#                     break
#             start += 1

# 是从后往前移动，不是从前往后移动，所以下面方法错误
# class Solution:
#     def rotate(self, nums, k) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         self.reserve(nums, 0, len(nums)-1)
#         self.reserve(nums, 0, len(nums)-k-1)
#         self.reserve(nums, len(nums)-k, len(nums)-1)
#
#     def reserve(self, nums, l, r):
#         while(l < r):
#             nums[l], nums[r] = nums[r], nums[l]
#             l += 1
#             r -= 1

# Runtime: 68 ms, faster than 35.06% of Python3 online submissions for Rotate Array.
# Memory Usage: 13.6 MB, less than 5.04% of Python3 online submissions for Rotate Array.
# 时间复杂度O(n)，空间复杂度O(1)。
# class Solution:
#     def rotate(self, nums, k) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         k = k % len(nums)   # 加上这里是为了防止k超过原本列表长度造成额外的工作或者错误
#         self.reserve(nums, 0, len(nums)-1)
#         self.reserve(nums, 0, k-1)
#         self.reserve(nums, k, len(nums)-1)
#
#     def reserve(self, nums, l, r):
#         while(l < r):
#             nums[l], nums[r] = nums[r], nums[l]
#             l += 1
#             r -= 1

# Runtime: 52 ms, faster than 81.17% of Python3 online submissions for Rotate Array.
# Memory Usage: 13.5 MB, less than 5.04% of Python3 online submissions for Rotate Array.
# 时间复杂度O(n)，空间复杂度O(n)。
# 不推荐此方法。
class Solution:
    def rotate(self, nums: 'List[int]', k: 'int') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        move_right = k % length
        nums[0:length] = nums[-move_right:] + nums[:-move_right]

nums = [1,2,3,4,5]
S = Solution()
S.rotate(nums,2)
print(nums)


