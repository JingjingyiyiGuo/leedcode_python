# This is a follow up of Shortest Word Distance.
# The only difference is now word1 could be the same as word2.
# Given a list of words and two words word1 and word2,
# return the shortest distance between these two words in the list.
# word1 and word2 may be the same and they represent two individual words in the list.
# For example,
# Assume that words = [“practice”, “makes”, “perfect”, “coding”, “makes”].
# Given word1 = “makes”, word2 = “coding”, return 1.
# Given word1 = “makes”, word2 = “makes”, return 3.
# Note: You may assume word1 and word2 are both in the list.
# class Solution:
#     def wordDistance(self, words, word1, word2) -> int:
#         point1 = -1   # 直接将上面对point的赋值改为-1，就可以避免再设置两个标签，来提高算法的效率
#         point2 = -1
#         flag = 0
#         distance = len(words)
#         if word1 == word2:
#             for i in range(len(words)):
#                 if words[i] == word1:
#                     if flag == 0:
#                         point1 = i
#                         flag = 1
#                     else:
#                         point2 = i
#                         flag = 0
#                     if point1 > -1 and point2 > -1:
#                         distance = min(distance, abs(point2 - point1))
#         else:
#             for i in range(len(words)):
#                 if words[i] == word1:
#                     point1 = i
#                 elif words[i] == word2:
#                     point2 = i
#                 # 这里相对于上面的写法，可以只写一次求最小值，因为在一轮里面也只会对一个指针赋值，不会漏掉比较
#                 if point1 > -1 and point2 > -1:
#                     distance = min(distance, abs(point2 - point1))
#         return distance

class Solution:
    def wordDistance(self, words, word1, word2) -> int:
        point1 = -1   # 直接将上面对point的赋值改为-1，就可以避免再设置两个标签，来提高算法的效率
        point2 = -1
        distance = len(words)
        for i in range(len(words)):
            if words[i] == word1:
                point1 = i
            if words[i] == word2:
                if word1 == word2:
                    point1 = point2   # 这里把point2的值巧妙的赋值给point1，避免两个指针值相等，思想值得学习
                point2 = i
            # 这里相对于上面的写法，可以只写一次求最小值，因为在一轮里面也只会对一个指针赋值，不会漏掉比较
            if point1 > -1 and point2 > -1:
                distance = min(distance, abs(point2 - point1))
        return distance

S = Solution()
words=["practice", "makes", "perfect", "coding", "makes"]
d = S.wordDistance(words, "coding", "practice")
print(d)
d = S.wordDistance(words, "makes", "coding")
print(d)
d = S.wordDistance(words, "makes", "makes")
print(d)