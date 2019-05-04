# 缺失的第一个正数
# 时间复杂度O(n)，空间复杂度O(1)
# Runtime: 36 ms, faster than 99.38% of Python3 online submissions for First Missing Positive.
# Memory Usage: 13.2 MB, less than 5.26% of Python3 online submissions for First Missing Positive.
import sys
# 遍历整个数组，将对应的数字尽可能放到指定的下标位置上，然后就可以从前往后遍历，寻找第一个不等于位序的值，
# 那个位序即为缺少的第一个整数
class Solution:
    def firstMissingPositive(self, a):
        for i in range(len(a)):
            # 必须是大于0，长度小于列表，且与对应位置存储的数字不同，才可以进行交换。
            while a[i] > 0 and a[i] <= len(a) and a[a[i]-1] != a[i]:
                a[a[i]-1],a[i] = a[i],a[a[i]-1]
        # 遍历寻找第一个与（位序+1）不同的值，那里缺少的值即为缺少的整数
        for i in range(0,len(a)):
            if a[i] != (i+1):
                return i+1
        return len(a)+1



S = Solution()
for line in sys.stdin:
    a = line.split(',')
    for i in range(len(a)):
        a[i] = int(a[i])
    r = S.firstMissingPositive(a)
    print(r)


