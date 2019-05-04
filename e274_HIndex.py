# Runtime: 40 ms, faster than 57.54% of Python3 online submissions for H-Index.
# Memory Usage: 13.3 MB, less than 5.88% of Python3 online submissions for H-Index.
# 时间复杂度是O(NlogN + N)，空间复杂度是O(N)。
# 排序+遍历
# class Solution(object):
#     def hIndex(self, citations):
#         """
#         :type citations: List[int]
#         :rtype: int
#         """
#         N = len(citations)
#         citations.sort()
#         h = 0
#         for i, c in enumerate(citations):
#             h = max(h, min(N - i, c))
#         return h

# Runtime: 36 ms, faster than 97.69% of Python3 online submissions for H-Index.
# Memory Usage: 13.1 MB, less than 5.88% of Python3 online submissions for H-Index.
# 时间复杂度是O(NlogN + logN)，空间复杂度是O(N)。
# 排序+二分
# class Solution(object):
#     def hIndex(self, citations):
#         """
#         :type citations: List[int]
#         :rtype: int
#         """
#         N = len(citations)
#         citations.sort()
#         l, r = 0, N - 1
#         H = 0
#         while l <= r:
#             mid = l + (r - l) // 2
#             H = max(H, min(citations[mid], N - mid))  # 这个公共条件提取的比较好，是优于我的代码的地方
#             if citations[mid] < N - mid:
#                 l = mid + 1
#             else:
#                 r = mid - 1
#         return H

# Runtime: 36 ms, faster than 97.69% of Python3 online submissions for H-Index.
# Memory Usage: 13.2 MB, less than 5.88% of Python3 online submissions for H-Index.
# 时间复杂度是O(NlogN + logN)，空间复杂度是O(N)。
# 排序+二分
# 与上面的方法相同，但是写得没有上面简洁，因为对其中的一个公共条件的提取不够到位
class Solution:
    def hIndex(self, citations) -> int:
        citations.sort()
        left = 0
        right = len(citations) - 1
        h = 0
        while left <= right:
            # 注意原来自己代码过不了的原因是没有在左边加left，只有加了才可以确保可以取到右边的数
            mid = left + (right - left) // 2
            if citations[mid] == len(citations) - mid:
                h = len(citations) - mid
                return h
            elif citations[mid] < len(citations) - mid:
                h = max(h,citations[mid])
                left = mid + 1
            elif citations[mid] > len(citations) - mid:
                h = max(h, len(citations) - mid)
                right = mid - 1
        return h

# Runtime: 36 ms, faster than 97.69% of Python3 online submissions for H-Index.
# Memory Usage: 13.1 MB, less than 5.88% of Python3 online submissions for H-Index.
# 这是时间复杂度最小的方法，为O(n)
# class Solution:
#     def hIndex(self, citations) -> int:
#         x = len(citations) + 1
#         bu = [0 for i in range(x)]     # 时间复杂度O(n)
#         for i in citations:            # 时间复杂度O(n)
#             if i < x:
#                 bu[i] += 1
#             else:
#                 bu[x-1] += 1
#         num = 0
#         for j in range(x-1,-1,-1):     # 时间复杂度O(n)
#             num += bu[j]
#             if num >= j:   # 这里不用跟上面一样各种取最大最小了，因为一旦计数大于等于value值了，再往前遍历就没有意义了，只会更小
#                 return j
#         return 0


citations = [3,0,6,1,5]  # 01356
# citations = [100]
S = Solution()
x = S.hIndex(citations)
print(x)
