# 算法思路：比较两个列表的第一位，删除较小的那个数；比较列表的最后一位，删除较大的那个数。在最终剩下的数里寻找中位数。
# Runtime: 116 ms, faster than 34.40% of Python3 online submissions for Median of Two Sorted Arrays.
# Memory Usage: 13.3 MB, less than 5.11% of Python3 online submissions for Median of Two Sorted Arrays.
# class Solution:
#     def findMedianSortedArrays(self, nums1, nums2) -> float:
#         while True:
#             if len(nums1) == len(nums2) == 1:
#                 median = (nums1[0] + nums2[0]) / 2.0
#                 return median
#             if len(nums1) == 0 and len(nums2) == 1:
#                 median = nums2[0]
#                 return median
#             if len(nums2) == 0 and len(nums1) == 1:
#                 median = nums1[0]
#                 return median
#             if len(nums1) == 0 and len(nums2) > 1:
#                 if len(nums2) % 2 == 1:
#                     median = nums2[int((len(nums2)-1)/2)]
#                     return median
#                 else:
#                     median = (nums2[int(len(nums2)/2)] + nums2[int(len(nums2)/2) - 1]) / 2.0
#                     return median
#             if len(nums1) > 1 and len(nums2) == 0:
#                 if len(nums1) % 2 == 1:
#                     median = nums1[int((len(nums1)-1)/2)]
#                     return median
#                 else:
#                     median = (nums1[int(len(nums1)/2)] + nums1[int(len(nums1)/2) - 1]) / 2.0
#                     return median
#             if nums1[0] < nums2[0]:
#                 del nums1[0]
#             else:
#                 del nums2[0]
#             if len(nums1) == 0 and len(nums2) != 0:
#                 del nums2[len(nums2)-1]
#                 continue
#             if len(nums1) != 0 and len(nums2) == 0:
#                 del nums1[len(nums1)-1]
#                 continue
#             if nums1[len(nums1)-1] >= nums2[len(nums2)-1]:
#                 del nums1[len(nums1)-1]
#             else:
#                 del nums2[len(nums2)-1]

# Runtime: 96 ms, faster than 69.50% of Python3 online submissions for Median of Two Sorted Arrays.
# Memory Usage: 13.4 MB, less than 5.11% of Python3 online submissions for Median of Two Sorted Arrays.
# class Solution:
#     def findMedianSortedArrays(self, nums1, nums2) -> float:
#         sorted_joined = sorted(nums1 + nums2)
#         if len(sorted_joined) % 2 == 0:
#             index = int(len(sorted_joined) / 2)
#             return (sorted_joined[index] + sorted_joined[index-1])/2
#         else:
#             index = (int(len(sorted_joined)/2))
#             return sorted_joined[index]
# leedcode中最快的方法，但是在我电脑跑出来与上述方法相同，因为毕竟都是用的同一种方法。
class Solution:
    def findMedianSortedArrays(self, nums1: 'List[int]', nums2: 'List[int]') -> 'float':
        s = nums1
        s.extend(nums2)
        s.sort()
        l = len(s)
        if l % 2 == 1:
            return s[l//2]
        return (s[l//2] + s[l//2-1]) / 2

nums1 = [1, 3]
nums2 = [2]
S = Solution()
x = S.findMedianSortedArrays(nums1,nums2)
print(x)
# nums1 = []
# nums2 = [1,2,3,4,5]
# S1 = Solution()
# x = S1.findMedianSortedArrays(nums1,nums2)
# print(x)