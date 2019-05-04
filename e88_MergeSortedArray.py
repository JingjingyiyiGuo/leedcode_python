# Runtime: 40 ms, faster than 79.62% of Python3 online submissions for Merge Sorted Array.
# Memory Usage: 13.1 MB, less than 5.09% of Python3 online submissions for Merge Sorted Array.
# 时间复杂度O(n)，空间复杂度O(1)。
# 这道题相当于在原位merge。
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        x = m + n - 1
        while x >= 0 and i >= 0 and j >= 0:
            if nums2[j] >= nums1[i]:
                nums1[x] = nums2[j]
                j -= 1
                x -= 1
            else:
                nums1[x] = nums1[i]
                i -= 1
                x -= 1
        while x >= 0 and j >= 0:
            nums1[x] = nums2[j]
            j -= 1
            x -= 1
# Runtime: 40 ms, faster than 79.62% of Python3 online submissions for Merge Sorted Array.
# Memory Usage: 13.3 MB, less than 5.09% of Python3 online submissions for Merge Sorted Array.
# 这么写只是比上面简洁了一些
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        x = m + n - 1
        while j >= 0:
            if i >= 0 and nums2[j] < nums1[i]:
                nums1[x] = nums1[i]
                i -= 1
                x -= 1
            else:
                nums1[x] = nums2[j]
                j -= 1
                x -= 1