class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        i = 0
        j = 0
        while True:
            if len(nums1) == len(nums2) == 1:
                median = (nums1[0] + nums2[0]) / 2.0
                return median
            if len(nums1) == 0 and len(nums2) == 1:
                median = nums2[0]
                return median
            if len(nums2) == 0 and len(nums1) == 1:
                median = nums1[0]
                return median
            if len(nums1) == 0 and len(nums2) > 1:
                if len(nums2) % 2 == 1:
                    median = nums2[int((len(nums2)+1)/2)]
                    return median
                else:
                    median = (nums2[int(len(nums2)/2)] + nums2[int(len(nums2)/2) - 1]) / 2.0
                    return median
            if len(nums1) > 1 and len(nums2) == 0:
                if len(nums1) % 2 == 1:
                    median = nums1[int((len(nums1)-1)/2)]
                    return median
                else:
                    median = (nums1[int(len(nums1)/2)] + nums1[int(len(nums1)/2) - 1]) / 2.0
                    return median
            if nums1[i] < nums2[j]:
                del nums1[i]
            else:
                del nums2[j]
            if nums1[len(nums1)-1-i] > nums2[len(nums2)-1-j]:
                del nums1[len(nums1)-1-i]
            else:
                del nums2[len(nums2)-1-i]

# nums1 = [1, 3]
# nums2 = [2]
# S = Solution()
# x = S.findMedianSortedArrays(nums1,nums2)
# print(x)
nums1 = [1,1,1]
nums2 = [1,1,1]
S1 = Solution()
x = S1.findMedianSortedArrays(nums1,nums2)
print(x)