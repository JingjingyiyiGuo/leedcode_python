# 暴力解决法：
# class Solution:
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         for i in range(0, len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] == 0:
#                     if nums[j] == target:
#                         return [i,j]
#                 if nums[i] + nums[j] == target:
#                     return [i,j]
# 哈希表解决法：
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict_num = {}
        for i in range(len(nums)):
            if nums[i] in dict_num:
                dict_num[nums[i]].append(i)
            else:
                dict_num[nums[i]] = [i]
        for i in nums:
            x = target - i
            if x == i:
                if len(dict_num[i]) > 1:
                    return [dict_num[i][0], dict_num[i][1]]
            else:
                if x in dict_num and dict_num[i] != dict_num[x]:
                    return [dict_num[i][0], dict_num[x][0]]





nums = [3,4,3,4]
target = 6
S = Solution()
result = S.twoSum(nums=nums,target=target)
print(result)