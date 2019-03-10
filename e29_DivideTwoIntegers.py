# 这样仅仅用减法会超时，所以该方法没有通过。
# 解这道题的时候还要注意数据的范围，需要考虑溢出的情况。
# class Solution:
#     def divide(self, dividend: int, divisor: int) -> int:
#         i = 0
#         if dividend >= 0 and divisor > 0:
#             sig = 1
#         elif dividend <= 0 and divisor < 0:
#             sig = 1
#         else:
#             sig = -1
#         dividend = abs(dividend)
#         divisor = abs(divisor)
#         if dividend < divisor:
#             return 0
#         if dividend == divisor:
#             return sig
#         if divisor == 1:
#             return sig * dividend if sig * dividend < 2**31 else 2**31-1
#         while dividend > 0:
#             dividend = dividend - divisor
#             if dividend >= 0:
#                 i += 1
#         if sig == 1:
#             return i
#         else:
#             return -i

# Runtime: 56 ms, faster than 59.69% of Python3 online submissions for Divide Two Integers.
# Memory Usage: 13.3 MB, less than 5.26% of Python3 online submissions for Divide Two Integers.
# 创造性的使用python数组方法来代替乘法，算是使用python求解算法题的一种偷懒的方法。
# class Solution:
#     def divide(self, fenzi, fenmu):
#         """
#         :type dividend: int
#         :type divisor: int
#         :rtype: int
#         """
#         flag = -1 if (fenzi <0 and fenmu >0) or (fenzi>0 and fenmu<0) else 1#定义一个flag判断正负
#         fenzi,fenmu = abs(fenzi),abs(fenmu)
#         if fenzi < fenmu:
#             return 0
#         if fenzi == fenmu:
#             return flag
#         if fenmu == 1: #防止2**31
#             return flag*fenzi if flag*fenzi < 2**31 else 2**31-1
#         return flag*len(range(fenmu,fenzi+1,fenmu))

# Runtime: 80 ms, faster than 18.65% of Python3 online submissions for Divide Two Integers.
# Memory Usage: 13.2 MB, less than 5.26% of Python3 online submissions for Divide Two Integers.
# 这里的方法感觉算是使用减法里面效率最高的方法了。
# 首先用加法成倍的加，提高效率，加不动了就减去已经算好的部分，对剩余部分递归求解。
# 这里应该是使用了
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        if dividend == 0:
            return 0
        if dividend < 0 and divisor < 0:
            return min(2147483647, self.helper(-dividend, -divisor))
        if dividend < 0 and divisor > 0:
            return max(-2147483648, -self.helper(-dividend, divisor))
        if dividend > 0 and divisor < 0:
            return max(-2147483648, -self.helper(dividend, -divisor))
        return min(2147483647, self.helper(dividend, divisor))

    def helper(self, dividend, divisor):
        if divisor > dividend:
            return 0

        div = divisor
        res = 1
        while div + div <= dividend:
            div += div
            res += res

        return res + self.helper(dividend - div, divisor)



nums1 = 10
nums2 = -3
S = Solution()
x = S.divide(nums1, nums2)
print(x)