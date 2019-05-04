# 返回值是一个int类型的整数，就是那个最大的积
# 输入是一个列表
# 双重for循环暴力求解：如果当前值比较大就记录下来，否则就继续往后计算
# 该方法提交后是超时的。
# class Solution:
#     def maxProduct(self, nums) -> int:
#         lar = nums[0]
#         for i in range(len(nums)):
#
#             for j in range(i, len(nums)):
#                 if i == j:
#                     cur = nums[i]
#                 else:
#                     cur *= nums[j]
#                 lar = max(lar,cur)
#         return lar

# Runtime: 72 ms, faster than 7.74% of Python3 online submissions for Maximum Product Subarray.
# Memory Usage: 14.6 MB, less than 5.52% of Python3 online submissions for Maximum Product Subarray.
# 下述为动态规划的方法：
# class Solution:
#     def maxProduct(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         temp=nums[0]  # 将最大的积初始化为列表的第一个数
#         n = len(nums)  # 计算列表的长度
#         M = [0 for i in range(n)]  #初始化一个跟列表长度相同的记录最大值的列表，其中每个值为0
#         m = [0 for i in range(n)]  #初始化一个跟列表长度相同的记录最小值的列表，其中每个值为0
#         for i in range(0,n):       #将数组从头到尾进行一次遍历
#             if i == 0:             #初始化一下M和m的第一个元素，都为列表的第一个元素
#                 M[i] = nums[i]
#                 m[i] = nums[i]
#             else:
#                 # 当前积为最大要为最大必定是同号相乘的结果，但是我们事先不知道当前数为正为负，
#                 # 因此，当前数的乘积最大为三种情况：当前数乘以当前数对应的最大值；当前数乘以当前数对应的最小值，当前数
#                 # 同理，当前数的乘积最小为三种情况：当前数乘以当前数对应的最大值；当前数乘以当前数对应的最小值，当前数
#                 M[i] = max(max(M[i-1]*nums[i], m[i-1]*nums[i]), nums[i])
#                 m[i]= min(min(M[i-1]*nums[i], m[i-1]*nums[i]), nums[i])
#             temp = max(temp,M[i])   #记录到i为止的最大积
#         return temp

class Solution:
    def maxProduct(self, A):
        B = A[::-1]   # 将列表A翻转
        for i in range(1, len(A)):
            A[i] *= A[i - 1] or 1
            B[i] *= B[i - 1] or 1
        return max(A + B)

# 还是不对，思考一下
class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:
            return False
        dp = nums[0]
        maxm = nums[0]
        minm = nums[0]
        for i in range(1,len(nums)):
            dp = max(maxm*nums[i],minm*nums[i],dp)
            max_temp = maxm
            maxm = max(maxm*nums[i],minm*nums[i],nums[i])
            minm = min(max_temp*nums[i],minm*nums[i],nums[i])
        dp = max(maxm,minm,dp)
        return dp

nums = [-1, 0, 1, 2, -1, -3]
S = Solution()
x = S.maxProduct(nums)
print(x)