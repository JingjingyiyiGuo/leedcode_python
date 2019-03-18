# 涉及到要求时间复杂度为log(n)的序列操作，优先考虑二分查找
# 旋转有序数列知识点：如果一个旋转有序数列的left的数小于right的数，那么这个序列本身是一个有序数列，没有旋转。
# 涉及到旋转有序数列，我们首先找的是那个最小的那个头，为了让它尽可能的在，
# 所以我们要尽可能动右边，因为最右边的数列永远在递增数列里。
# Runtime: 40 ms, faster than 65.53% of Python3 online submissions for Search in Rotated Sorted Array.
# Memory Usage: 13.2 MB, less than 5.96% of Python3 online submissions for Search in Rotated Sorted Array.
class Solution:
    def search(self, nums, target) -> int:
        # 先用二分查找找到有序数列的头部
        left = 0
        right = len(nums) - 1
        while left < right:   # 这里不用等于，因为一旦出现了等于的情况就不用操作了
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1    # 因为那个大的数不可能是数列头，所以直接加1
            else:
                right = mid    # 因为那个小的数可能是数列头，所以只让等于mid，并不减1. 要用贪心的思想前进和后退
        head = left
        rem = self.binarySearch(nums[:head], target)
        if rem == -1:
            rem = self.binarySearch(nums[head:], target)
            if rem != -1:
                return head + rem
        return rem

    def binarySearch(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:   # 这里需要等于，因为等于的时候要去判断target相等，然后return
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
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