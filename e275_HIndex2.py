# Runtime: 44 ms, faster than 85.65% of Python3 online submissions for H-Index II.
# Memory Usage: 16.7 MB, less than 7.69% of Python3 online submissions for H-Index II.
# 时间复杂度O(log(n))
class Solution:
    def hIndex(self, citations) -> int:
        left = 0
        right = len(citations) - 1
        h = 0
        while left <= right:
            mid = left + (right - left) // 2
            h = max(h, min(citations[mid], len(citations)-mid))
            if citations[mid] == len(citations)-mid:
                return citations[mid]
            elif citations[mid] < len(citations)-mid:
                left = mid + 1
            else:
                right = mid -1
        return h

# Runtime: 44 ms, faster than 85.65% of Python3 online submissions for H-Index II.
# Memory Usage: 16.8 MB, less than 7.69% of Python3 online submissions for H-Index II.
class Solution:
    def hIndex(self, citations) -> int:
        left = 0
        right = len(citations) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if citations[mid] == len(citations)-mid:
                return citations[mid]
            elif citations[mid] < len(citations)-mid:
                left = mid + 1
            else:
                right = mid -1
        return len(citations) - left  # 因为我们会一直缩小范围到mid==left，而长度恰好是h的限制因素，所以可以直接返回长度

# Runtime: 44 ms, faster than 85.65% of Python3 online submissions for H-Index II.
# Memory Usage: 16.5 MB, less than 7.69% of Python3 online submissions for H-Index II
class Solution:
    def hIndex(self, citations) -> int:
        left = 0
        right = len(citations) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if citations[mid] == len(citations)-mid:
                return citations[mid]
            elif citations[mid] < len(citations)-mid:
                left = mid + 1
            else:
                right = mid -1
        return len(citations) - (right + 1)  # 因为right会小于left，所以如果用right，就要加1