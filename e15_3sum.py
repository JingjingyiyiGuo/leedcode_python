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

# 这个方法提交通过了，但是效率比较低
# 13200ms, 17.9MB
# class Solution:
#     def threeSum(self, nums):
#         dict_num = {}
#         result = []
#         for i in range(len(nums)):
#             if nums[i] in dict_num:
#                 dict_num[nums[i]].append(i)
#             else:
#                 dict_num[nums[i]] = [i]
#         for i in range(len(nums)):
#             new_tar = 0 - nums[i]
#             for j in range(i+1, len(nums)):
#                 tar = new_tar - nums[j]
#                 if tar == nums[j] and tar != nums[i]:
#                     if len(dict_num[nums[j]]) > 1 :
#                         result_temp = sorted([nums[i],nums[j],tar])
#                         if result_temp in result:
#                             pass
#                         else:
#                             result.append(result_temp)
#                 elif tar == nums[j] and tar == nums[i]:
#                     if len(dict_num[nums[j]]) > 2 :
#                         result_temp = sorted([nums[i],nums[j],tar])
#                         if result_temp in result:
#                             pass
#                         else:
#                             result.append(result_temp)
#                 else:
#                     if tar in dict_num and dict_num[tar] != dict_num[nums[j]] and dict_num[tar] != dict_num[nums[i]]:
#                         result_temp = sorted([nums[i],nums[j],tar])
#                         if result_temp in result:
#                             pass
#                         else:
#                             result.append(result_temp)
#         return result

# Runtime: 1600 ms, faster than 29.78% of Python3 online submissions for 3Sum.
# Memory Usage: 16.8 MB, less than 20.61% of Python3 online submissions for 3Sum.
# 效率比上面的方法高好多。
#
class Solution:
    def threeSum(self, num):
        num.sort()
        res = []
        for i in range(len(num)-2):
            if i == 0 or num[i] > num[i-1]:
                left = i + 1; right = len(num) - 1
                while left < right:
                    if num[left] + num[right] == -num[i]:
                        res.append([num[i], num[left], num[right]])
                        left += 1; right -= 1
                        while left < right and num[left] == num[left-1]: left +=1
                        while left < right and num[right] == num[right+1]: right -= 1
                    elif num[left] + num[right] < -num[i]:
                        while left < right:
                            left += 1
                            if num[left] > num[left-1]: break
                    else:
                        while left < right:
                            right -= 1
                            if num[right] < num[right+1]: break
        return res



# nums = [-1, 0, 1, 2, -1, -4]
nums = [0,0]
S = Solution()
x = S.threeSum(nums)
print(x)
