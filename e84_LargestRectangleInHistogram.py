# nums = [4,2,0,3,2,4,3,4]  验证的时候出了错误
# 因为用的解题思路是e11里面的思路
# 该题目与e11的区别，e11只考虑边界的最小值，并不考虑中间的最小值，即不会受到它们的限制
# 改题目会收中间最小值的影响
# class Solution:
#     def largestRectangleAreaError(self, heights) -> int:
#         if len(heights) < 1:
#             return 0
#         if len(heights) == 1:
#             return heights[0]
#         lar = 0
#         i = 0
#         j = len(heights) - 1
#         while i <= j:
#             area = (j - i + 1) * min(heights[i:j+1])
#             # print("(j - i + 1):", j - i + 1)
#             # print("min:", min(heights[i:j]))
#             if area > lar:
#                 lar = area
#             # print("lar:", lar)
#             if heights[i] < heights[j]:
#                 i += 1
#             else:
#                 j -= 1
#         return lar

# 问题解析：https://www.cnblogs.com/ganganloveu/p/4148303.html
# 如果是递增数列，则该题目很好解
# 现在不是递增数列，所以我们要用栈来创造递增数列
# Runtime: 80 ms, faster than 28.73% of Python3 online submissions for Largest Rectangle in Histogram.
# Memory Usage: 14.1 MB, less than 88.20% of Python3 online submissions for Largest Rectangle in Histogram.
class Solution:
    def largestRectangleArea(self, heights) -> int:
        ret = 0   # 用来存储最大面积，这里初始化为0
        stack = []   # 初始化栈
        for i in range(0, len(heights)):   # 扫描数组的头到尾，构建栈
            if not stack or stack[-1] < heights[i]:  # 如果栈为空，或者栈顶元素小于下一元素，则递增序列，进栈
                stack.append(heights[i])
            else:   # 否则要一直出栈，直到找到满足条件的值后，将那个值重复多次进栈，出了几个，就得进几个，同时还得进当前值
                count = 0  # 用来计数出栈几个元素
                while stack and stack[-1] > heights[i]:
                    count += 1  # 发现一个不满足条件的，计数
                    ret = max(ret, stack[-1] * count)   # 当前栈顶元素乘以这次调整出栈的元素，即为当前局部递增数列的最大面积
                    stack.pop()  # 发现一个不满足条件的，出栈
                while count:   # 出几个就进几个，进的为当前被比较元素
                    stack.append(heights[i])
                    count -= 1
                stack.append(heights[i])  # 最后将本次被比较的数进栈
        count = 1
        while stack: # 当前栈为递增数列，按递增数列规则，计算最大面积
            ret = max(ret, stack[-1] * count)  # 时刻比较观察是否为最大值
            stack.pop()
            count += 1

        return ret

nums = [2,1,5,6,2,3]
# nums = [4,2,0,3,2,4,3,4]
S = Solution()
x = S.largestRectangleArea(nums)
print(x)