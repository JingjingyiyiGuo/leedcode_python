# Given a list of words and two words word1 and word2,
# return the shortest distance between these two words in the list.
# Assume that words=["practice", "makes", "perfect", "coding", "makes"]
# Given word1 = “coding”, word2 = “practice”, return 3.
# Given word1 = "makes", word2 = "coding", return 1.
# 时间复杂度O(n)，空间复杂度O(1)
# class Solution:
#     def wordDistance(self, words, word1, word2) -> int:
#         point1 = 0
#         point2 = 0
#         flag1 = 0
#         flag2 = 0
#         distance = len(words)
#         for i in range(len(words)):
#             if words[i] == word1:
#                 point1 = i
#                 flag1 += 1
#                 if flag1 > 0 and flag2 > 0:
#                     distance = min(distance, abs(point2 - point1))
#             if words[i] == word2:
#                 point2 = i
#                 flag2 += 1
#                 if flag1 > 0 and flag2 > 0:
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
            elif words[i] == word2:
                point2 = i
            # 这里相对于上面的写法，可以只写一次求最小值，因为在一轮里面也只会对一个指针赋值，不会漏掉比较
            if point1 > -1 and point2 > -1:
                distance = min(distance, abs(point2 - point1))
        return distance

# class Solution:
#     def wordDistance(self, words, word1, word2) -> int:
#         point = -1   # 将两个指针的使用变成一个，代码更简洁
#         distance = len(words)
#         for i in range(len(words)):
#             if words[i] == word1 or words[i] == word2:
#                 if point > -1 and words[point] != words[i]:
#                     distance = min(distance, i - point)
#                 point = i  # 只要有词相等了，point的位置就要变化
#         return distance




S = Solution()
words=["practice", "makes", "perfect", "coding", "makes"]
d = S.wordDistance(words, "coding", "practice")
print(d)
d = S.wordDistance(words, "makes", "coding")
print(d)