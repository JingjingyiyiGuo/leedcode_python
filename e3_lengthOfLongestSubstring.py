# 暴力解决法
# class Solution:
#     def lengthOfLongestSubstring(self, s: 'str') -> 'int':
#         rem_len = 0
#         if len(s) < 1:
#             return 0
#         rem = []
#         rem.append(s[0])
#         for i in range(1,len(s)):
#             for j in range(0,len(s)-i):
#                 if s[i+j] in rem:
#                     if rem_len < len(rem):
#                         rem_len = len(rem)
#                     rem = []
#                     rem.append(s[i])
#                     break
#                 else:
#                     rem.append(s[i+j])
#                 # print(rem)
#         if rem_len < len(rem):
#             rem_len = len(rem)
#         return rem_len


# 应该用dijistic
class Solution:
    def lengthOfLongestSubstring(self, s: 'str') -> 'int':
        pass


s = "jbpnbwwd"
S = Solution()
x = S.lengthOfLongestSubstring(s)
print(x)

# 在答案中看到的python中最快的代码，供学习
# def lengthOfLongestSubstring(self, s: 'str') -> 'int':
#     maxlen = 0
#     currentlen = 0
#     indHash = {}
#     leftside = -1
#     ls = len(s)
#     for ind, ch in enumerate(s):
#         if (ch in indHash) and (leftside < indHash[ch]):
#             leftside = indHash[ch];
#         currentlen = ind - leftside;
#         if currentlen > maxlen:
#             maxlen = currentlen
#         indHash[ch] = ind
#     currentlen = ls - leftside - 1
#     if currentlen > maxlen:
#         maxlen = currentlen
#     return maxlen