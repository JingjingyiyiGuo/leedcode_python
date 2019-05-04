# his is a follow up of Shortest Word Distance. The only difference is now
# you are given the list of words and your method will be calledrepeatedly
# many times with different parameters. How would you optimize it?
# Design a class which receives a list of words in the constructor,
# and implements a method that takes two words word1 and word2 and
# return the shortest distance between these two words in the list.
# For example,
# Assume that words = [“practice”, “makes”, “perfect”, “coding”, “makes”].
# Given word1 = “coding”, word2 = “practice”, return 3.
# Given word1 = “makes”, word2 = “coding”, return 1.
# Note: You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
# 因为是重复调用，所以每个词最好存储了自己的位序，用hash表。
# 待存储好位序后，问题变成了求两个有序数组之差的最小值，设置两个指针，每次值小的加1，这样就是在把值往一起凑。
# 这里的思想可以往排序上想。
# https://blog.csdn.net/qq508618087/article/details/50887452
class Solution:
    def wordDistance(self, words, word1, word2) -> int:
        words_dict = {}
        for i in range(len(words)):
            if words[i] in words_dict:
                words_dict[words[i]].append(i)
            else:
                words_dict[words[i]] = [i]
        list1 = words_dict[word1]
        list2 = words_dict[word2]
        distance = len(words)
        i = 0
        j = 0
        while i < len(list1) and j < len(list2):
            distance = min(distance, abs(list1[i]-list2[j]))
            if list1[i] < list2[j]:
                i += 1
            else:
                j += 1
        return distance


S = Solution()
words=["practice", "makes", "perfect", "coding", "makes"]
d = S.wordDistance(words, "coding", "practice")
print(d)
d = S.wordDistance(words, "makes", "coding")
print(d)