# 时间复杂度O(n^2)，因为del的时间复杂度为O(n)。
# Runtime: 52 ms, faster than 15.34% of Python3 online submissions for Remove Element.
# Memory Usage: 13.2 MB, less than 5.09% of Python3 online submissions for Remove Element.
class Solution:
    def removeElement(self, nums, val) -> int:
        i = 0
        while True:
            if i >= len(nums):
                break
            if nums[i] == val:
                del nums[i]
                continue
            i += 1
        return len(nums)

# 时间复杂度为O(n)
# Runtime: 36 ms, faster than 99.21% of Python3 online submissions for Remove Element.
# Memory Usage: 13.2 MB, less than 5.09% of Python3 online submissions for Remove Element.
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        j = 0
        for i in range(len(nums)):
            if nums[i]==val:
                pass
            else:
                nums[j]=nums[i]
                j+=1
        return j

# 利用了希尔排序远距离交换的思想，平均速度应该快于上一个算法。
# Runtime: 36 ms, faster than 99.21% of Python3 online submissions for Remove Element.
# Memory Usage: 13.3 MB, less than 5.09% of Python3 online submissions for Remove Element.
class Solution:
    def removeElement(self, nums, val) -> int:
        n = len(nums) - 1
        i = 0
        while i <= n:
            if nums[i] == val:
                nums[i] = nums[n]
                n -= 1
            else:
                i += 1
        return i

# 这个方法就是把第二个方法倒着来了。
# Runtime: 36 ms, faster than 99.21% of Python3 online submissions for Remove Element.
# Memory Usage: 13.3 MB, less than 5.09% of Python3 online submissions for Remove Element.
class Solution:
    def removeElement(self, nums: 'List[int]', val: 'int') -> 'int':
        length = len(nums)
        if length == 0:
            return 0
        right = length - 1

        for i in range(right, -1, -1):
            if nums[i] == val:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1

        return max(right + 1, 0)

nums = [3,2,2,3]
S = Solution()
x = S.removeElement(nums,2)
print(x)