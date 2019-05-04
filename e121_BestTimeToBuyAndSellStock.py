# Runtime: 44 ms, faster than 82.77% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 13.8 MB, less than 5.08% of Python3 online submissions for Best Time to Buy and Sell Stock.
# 目的，保证买入价格是最低价，卖出价格是最高价
# 遍历了一次，时间复杂度为O(n)，空间复杂度O(n)。
# 只需要遍历一次数组，通过一个变量记录当前最低价格，同时算出此次交易利润，并与当前最大值比较就可以了。
class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices) == 0:   # 如果价格列表为空，则返回利润为0
            return 0
        begin = prices[0]  # 初始化价格列表的第一项为买入项
        result = 0         # 初始化利润为0
        for p in prices:   # 遍历价格列表中的每一个价格
            result = max(result, p-begin)  # 用当前价格减去买入价格，记录最大利润
            begin = min(begin,p)           # 往后走，只要碰到更低的买入利润，则重新为买入价格赋值
        return result