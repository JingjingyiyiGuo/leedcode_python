# Runtime: 44 ms, faster than 67.10% of Python3 online submissions for Single Number.
# Memory Usage: 14.7 MB, less than 5.05% of Python3 online submissions for Single Number.
# 时间复杂度O(n)，空间复杂度O(1)
# 利用了异或相同为0，不同为自身的性质，还有可以交换的性质。
class Solution:
    def singleNumber(self, nums) -> int:
        result = 0
        for i in range(len(nums)):
            result ^= nums[i]
        return result

# Runtime: 1172 ms, faster than 12.09% of Python3 online submissions for Single Number.
# Memory Usage: 14.7 MB, less than 5.05% of Python3 online submissions for Single Number.
# 时间复杂度O(n^2)，空间复杂度O(n)
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        no_duplicate_list = []
        for i in nums:
            if i not in no_duplicate_list:
                no_duplicate_list.append(i)
            else:
                no_duplicate_list.remove(i)
        return no_duplicate_list.pop()

# Runtime: 48 ms, faster than 44.87% of Python3 online submissions for Single Number.
# Memory Usage: 15.1 MB, less than 5.05% of Python3 online submissions for Single Number.
# python中的字典有类似于哈希表的功能，所以这里的时间复杂度O(n)，空间复杂度O(n)
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_table = {}
        for i in nums:
            try:  # 如果字典中有，则弹出
                hash_table.pop(i)
            except:  # 如果字典中没有，则存进去
                hash_table[i] = 1
        return hash_table.popitem()[0]

# Runtime: 56 ms, faster than 29.22% of Python3 online submissions for Single Number.
# Memory Usage: 15 MB, less than 5.05% of Python3 online submissions for Single Number.
# set()集合操作可以直接筛选出单个的元素，set()背后的机制是二叉查找树，时间复杂度为O(log(n)).
# set相对于list，是拿空间换时间，所以空间复杂度比较高。
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2 * sum(set(nums)) - sum(nums)