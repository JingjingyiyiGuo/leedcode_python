# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
# intervals为区间列表；返回值也是一个区间列表
# Runtime: 56 ms, faster than 79.61% of Python3 online submissions for Insert Interval.
# Memory Usage: 16.7 MB, less than 5.52% of Python3 online submissions for Insert Interval
# class Solution:
#     def insert(self, intervals, newInterval):
#         """
#         :type intervals: List[Interval]   区间列表
#         :type newInterval: Interval       新区间
#         :rtype: List[Interval]            返回值也为区间列表
#         """
#         intervals.append(newInterval)      # 首先在区间列表末尾添加新区间
#         l = len(intervals)                 # 计算区间列表的长度
#         res = []   # 用来存储新的区间列表
#         # 按每个区间的起始值对当前区间进行排序
#         intervals = sorted(intervals, key = lambda intervals:intervals.start)
#         # 设置两个指针，分别指向第一个区间的首尾值
#         low = intervals[0].start
#         high = intervals[0].end
#         # 遍历区间中的每个区间
#         for i in range(1, l):
#             # 如果第i个区间的start小于第i-1个区间的high，则该区间是要被合并的
#             # 所以利用max函数取当前区间的末尾和前一区间的末尾最大值作为high
#             # 一直到区间不重叠后，才会进入else被添加进去
#             if intervals[i].start <= high:
#                 high = max(high, intervals[i].end)
#             else:
#                 res.append([low, high])   # 将不重叠的首尾值存储起来
#                 low = intervals[i].start  # 让指针指向当前的首尾值
#                 high = intervals[i].end
#         res.append([low, high])   # 将最后一组的首尾值存储起来
#         return res

# 以下是当前leedcode上提交的效率最高的代码，速度为44ms
# 待分析
class Solution:
    def insert(self, intervals, newInterval):
        '''
        ans = []
        insert_pos = 0
        for interval in intervals:
            if interval.end < newInterval.start:
                ans.append(interval)
                insert_pos += 1
            elif interval.start > newInterval.end:
                ans.append(interval)
            else:
                newInterval.start = min(interval.start, newInterval.start)
                newInterval.end = max(interval.end, newInterval.end)
        ans.insert(insert_pos, newInterval)
        return ans
        '''
        lo, hi = 0, len(intervals)
        while lo < hi:
            mid = (lo + hi) // 2
            if intervals[mid].end < newInterval.start:
                lo = mid + 1
            else:
                hi = mid

        left_interval_index = lo

        # find the highest start that is lower than newInterval.end
        lo, hi = left_interval_index, len(intervals)
        while lo < hi:
            mid = (lo + hi) // 2
            if intervals[mid].start <= newInterval.end:
                lo = mid + 1
            else:
                hi = mid

        right_interval_index = lo - 1

        if left_interval_index < len(intervals):
            newInterval.start = min(newInterval.start, intervals[left_interval_index].start)
        if right_interval_index >= 0:
            newInterval.end = max(newInterval.end, intervals[right_interval_index].end)

        return intervals[:left_interval_index] + [newInterval] + intervals[right_interval_index + 1:]

intervals = []
a = Interval(1,3)
b = Interval(6,9)
intervals.append(a)
intervals.append(b)
newInterval = Interval(2,5)
S = Solution()
x = S.insert(intervals,newInterval)
print(x)

# intervals2 = [[1,2],[3,5],[6,7],[8,10],[12,16]]
# newInterval2 = [4,8]
# x2 = S.insert(intervals2,newInterval2)
# print(x2)