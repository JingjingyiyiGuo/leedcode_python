# Runtime: 68 ms, faster than 16.24% of Python3 online submissions for Bulls and Cows.
# Memory Usage: 13.2 MB, less than 6.15% of Python3 online submissions for Bulls and Cows.
# 时间复杂度O(n)，空间复杂度O(n)。
# class Solution:
#     def getHint(self, secret: str, guess: str) -> str:
#         bull = 0
#         bull_list = []
#         cow_dict = {}
#         cow = 0
#         for i in range(len(secret)):
#             if secret[i] == guess[i]:
#                 bull += 1
#                 bull_list.append(i)
#             else:
#                 if secret[i] in cow_dict:
#                     cow_dict[secret[i]].append(i)
#                 else:
#                     cow_dict[secret[i]] = [i]
#         for i in range(len(secret)):
#             if i not in bull_list and guess[i] in cow_dict:
#                 if cow_dict[guess[i]] != []:
#                     cow_dict[guess[i]].pop()
#                     cow += 1
#         return str(bull)+'A'+str(cow)+'B'

# Runtime: 60 ms, faster than 32.49% of Python3 online submissions for Bulls and Cows.
# Memory Usage: 13.2 MB, less than 6.15% of Python3 online submissions for Bulls and Cows.
# 时间复杂度O(n)，空间复杂度O(1)。
# 比上面的方法快，占用的空间还小。
# class Solution:
#     def getHint(self, secret: str, guess: str) -> str:
#         bull = 0
#         cow = 0
#         nums = [0 for i in range(10)]
#         for i in range(len(secret)):
#             if secret[i] == guess[i]:
#                 bull += 1
#             else:  # 这里通过记录数字个数的方式来记录同数不同位，方法很巧妙。
#                 if nums[int(secret[i])] < 0:
#                     cow += 1
#                 if nums[int(guess[i])] > 0:
#                     cow += 1
#                 nums[int(secret[i])] += 1
#                 nums[int(guess[i])] -= 1
#         return str(bull)+'A'+str(cow)+'B'

# 还不太理解
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        unmatched_secret = [0] * 10
        unmatched_guess = [0] * 10
        bulls = 0
        for x, y in zip(secret, guess):
            x, y = int(x), int(y)
            if x == y:
                bulls += 1
            else:
                unmatched_secret[x] += 1
                unmatched_guess[y] += 1
        cows = sum(min(unmatched_secret[i], unmatched_guess[i]) for i in range(10))
        return f'{bulls}A{cows}B'


# class Solution:
#     def getHint(self, secret: str, guess: str) -> str:
#         bulls = sum(map(operator.eq, secret, guess))
#         both = sum(min(secret.count(x), guess.count(x)) for x in set(guess))
#         return '%dA%dB' % (bulls, both - bulls)


S = Solution()
x = S.getHint('1123','0111')
print(x)