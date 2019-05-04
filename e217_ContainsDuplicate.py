# Runtime: 44 ms, faster than 93.10% of Python3 online submissions for Contains Duplicate.
# Memory Usage: 18.7 MB, less than 25.52% of Python3 online submissions for Contains Duplicate.
# 时间复杂度O(n)，空间复杂度O(n)。因为set求并集的时间复杂度为O(n)。
class Solution:
    def containsDuplicate(self, nums) -> bool:
        new = set(nums)
        if len(new) == len(nums):
            return False
        else:
            return True

# 方法一：如果用双层for循环来做这个问题，叫做线性搜索方法，会超时。时间复杂度O(n^2)，空间复杂度O(1)。

# 方法二：排序，如果有任何重复的元素，在排序后他们是连续的。时间复杂度O(nlogn)，空间复杂度O(1)。
# 这里的实现通过对原始数组进行排序来修改它。 通常，修改输入不是一个好习惯，除非调用者清楚输入将被修改。
# 人们可以制作nums的副本并在副本上操作。

# 方法三：哈希表：Utilize a dynamic data structure that supports fast search and insert operations.
# 时间复杂度O(n)，空间复杂度O(n)。方便插入和搜索。
# 回顾一下二叉搜索树也方便插入和搜索，其搜索的时间复杂度为O(logn)。




S = Solution()
nums = [1,2,3,1]
x = S.containsDuplicate(nums)
print(x)