# 暴力方法：超时
# class Solution:
#     def threeSum(self, nums):
#         result = []
#         nums = sorted(nums)
#         dict_num = {}
#         for i in range(len(nums)):
#             if nums[i] in dict_num:
#                 dict_num[nums[i]].append(i)
#             else:
#                 dict_num[nums[i]] = [i]
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 temp = 0 - nums[i] - nums[j]
#                 if temp in dict_num:
#                     if len(dict_num[temp]) == 1 and dict_num[temp][0] > j:
#                         result_temp = [nums[i],nums[j],temp]
#                         if result_temp in result:
#                             pass
#                         else:
#                             result.append(result_temp)
#                     if len(dict_num[temp]) != 1:
#                         for k in range(len(dict_num[temp])):
#                             if dict_num[temp][k] > j:
#                                 result_temp = [nums[i],nums[j],temp]
#                                 if result_temp in result:
#                                     pass
#                                 else:
#                                     result.append(result_temp)
#         return result

class Solution:
    def threeSum(self, nums):
        dict_num = {}
        result = []
        for i in range(len(nums)):
            if nums[i] in dict_num:
                dict_num[nums[i]].append(i)
            else:
                dict_num[nums[i]] = [i]
        for i in range(len(nums)):
            new_tar = 0 - nums[i]
            for j in range(i+1, len(nums)):
                tar = new_tar - nums[j]
                if tar == nums[j]:
                    if len(dict_num[nums[j]]) > 1 :
                        result_temp = sorted([nums[i],nums[j],tar])
                        if result_temp in result:
                            pass
                        else:
                            result.append(result_temp)
                else:
                    if tar in dict_num and dict_num[tar] != dict_num[nums[j]] and dict_num[tar] != dict_num[nums[i]]:
                        result_temp = sorted([nums[i],nums[j],tar])
                        if result_temp in result:
                            pass
                        else:
                            result.append(result_temp)
        return result



# nums = [-1, 0, 1, 2, -1, -4]
nums = [0,0]
S = Solution()
x = S.threeSum(nums)
print(x)
