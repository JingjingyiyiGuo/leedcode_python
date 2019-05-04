# Runtime: 40 ms, faster than 98.86% of Python3 online submissions for Best Time to Buy and Sell Stock II.
# Memory Usage: 13.9 MB, less than 5.06% of Python3 online submissions for Best Time to Buy and Sell Stock II.
# 遍历了一次，时间复杂度为O(n)，空间复杂度O(n)。
# 目的：总利润最高，只要卖出比买入高，就抓住机会进行交易。则会保证总利润最高。
# （注意这是在没有重复交易的前提下，即每次买入时，必须卖出前面的股票）
# 因为不限制交易次数，我们在第i天买入，如果发现i + 1天比i高，那么就可以累加到利润里面。
class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices) == 0:  # 如果价格列表为空，则返回利润为0
            return 0
        result = 0            # 初始化价格列表的第一项为买入项
        begin = prices[0]     # 初始化利润为0
        for p in prices:      # 遍历价格列表中的每一个价格
            if p > begin:     # 如果当前价格大于开始价格，则累加入收入
                result += p - begin  # 累加操作，即卖出操作
                begin = p     # 因为累加进收入，证明卖出了，所以更新当前位置为买入点。即卖出后马上买入
            else:
                begin = min(begin, p)   # 如果当前价格高于前面价格，则前面不买入，更新当前最小值为买入值
        return result

nums = [1,3,2]
S = Solution()
a = S.maxProfit(nums)
print(a)