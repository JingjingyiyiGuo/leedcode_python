# 题目地址：https://www.lintcode.com/problem/find-the-celebrity/description
"""
The knows API is already defined for you.
@param a, person a
@param b, person b
@return a boolean, whether a knows b
you can call Celebrity.knows(a, b)
"""
# 超时
class Solution:
    # @param {int} n a party with n people
    # @return {int} the celebrity's label or -1
    def findCelebrity(self, n):
        i = 0
        j = 0
        while i < n and j < n:
            j = 0
            if i == j:
                j += 1
            elif Celebrity.knows(i, j):
                i += 1
            else:
                j = 1
                while j < n:
                    if Celebrity.knows(i, j):
                        break
                    else:
                        j += 1
                if j == n:
                    for x in range(n):
                        if x == i:
                            continue
                        if Celebrity.knows(x, i):
                            continue
                        else:
                            break
                    if x == n:
                        return x
                    else:
                        return -1
        return -1

# 下述方法正确
class Solution:
    # @param {int} n a party with n people
    # @return {int} the celebrity's label or -1
    def findCelebrity(self, n):
        if n < 1:
            return -1
        if n == 1:
            return 0
        k = 0
        for i in range(1,n):
            if Celebrity.knows(k, i):
                k = i
        for i in range(0, n):
            if k != i and (not Celebrity.knows(i, k) or Celebrity.knows(k, i)):
                return -1
        return k
