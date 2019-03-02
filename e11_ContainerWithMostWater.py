# 暴力求解：
# class Solution:
#     def maxArea(self, height) -> int:
#         area = 0
#         for i in range(len(height)):
#             for j in range(i+1, len(height)):
#                 area_temp = min(height[i],height[j]) * (j - i)
#                 if area_temp > area:
#                     area = area_temp
#         return area

# 对两个决定结果的条件进行贪心控制：
class Solution:
    def maxArea(self, height) -> int:
        end = len(height) - 1
        start = 0
        area = 0
        while start < end:
            area_temp = min(height[start],height[end]) * (end - start)
            if area_temp > area:
                area = area_temp
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return area


nums = [1,8,6,2,5,4,8,3,7]
S = Solution()
x = S.maxArea(nums)
print(x)