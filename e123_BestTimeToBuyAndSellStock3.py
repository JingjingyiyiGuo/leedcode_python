# 注意不可以同时有多个交易，也就是再下次买之前，必须卖掉前面买的。
class Solution:
    # 此方法不正确，因为有时候中间股票虽然降价了，但是可以不卖出，而是等待下次价格回升卖的更高。
    def maxProfitError(self, prices) -> int:
        if len(prices) <= 1:
            return 0
        begin = prices[0]
        result = []
        for p in prices:
            if p > begin:
                result.append(p-begin)
                begin = p
            else:
                result.append(0)
                begin = min(begin, p)
        print(result)
        sum_p = [0 for i in range(len(result))]
        i = 0
        j = 0
        for r in result:
            if r != 0:
                sum_p[i] += r
                j += 1
            else:
                i += 1
                i += j
                j = 0
        print(sum_p)
        sum_p.sort()
        print(sum_p)
        rel = sum_p[-1] + sum_p[-2]
        return rel

    # 最多允许两次不相交的交易，也就意味着这两次交易间存在某一分界线，
    # 考虑到可只交易一次，也可交易零次，故分界线的变化范围为第一天至最后一天，
    # 只需考虑分界线两边各自的最大利润，最后选出利润和最大的即可。
    # 这种方法抽象之后则为首先将 [1,n] 拆分为 [1,i] 和 [i+1,n],
    # 参考卖股票系列的第一题计算各自区间内的最大利润即可。[1,i] 区间的最大利润很好算，
    # 但是如何计算 [i+1,n] 区间的最大利润值呢？难道需要重复 n 次才能得到？
    # 注意到区间的右侧 n 是个不变值，我们从 [1, i] 计算最大利润是更新波谷的值，
    # 那么我们可否逆序计算最大利润呢？这时候就需要更新记录波峰的值了.
    # 原文：https://blog.csdn.net/arthurzhang73/article/details/80633679
    # Runtime: 64 ms, faster than 57.26% of Python3 online submissions for Best Time to Buy and Sell Stock III.
    # Memory Usage: 14.3 MB, less than 9.83% of Python3 online submissions for Best Time to Buy and Sell Stock III.
    def maxProfit(self, prices) -> int:
        if len(prices) <= 1:  # 如果价格列表为空或者只有一个值，则返回利润为0
            return 0
        # 从前往后计算到当前位置，买卖股票的最大利润为多少，计入列表的相应位置
        resultfront = [0 for i in range(len(prices))]  # 初始化利润列表为0
        result = 0   # 初始化当前最大利润为0
        begin = prices[0]   # 初始化第一项为最初买入价格
        for r in range(len(prices)):  # 计算到当前位置买卖股票的最大利润
            result = resultfront[r] = max(result, prices[r] - begin)  # 计算存储最大利润
            begin = min(begin, prices[r])                             # 更新买入价格

        # 从后往前计算到当前位置，买卖股票的最大利润为多少，计入列表的相应位置
        resultafter = [0 for i in range(len(prices))]   # 初始化利润列表为0
        result = 0    # 初始化当前最大利润为0
        end = prices[-1]   # 初始化最后一项为最后卖出价格
        for j in range(len(prices)-1,-1,-1):  # 倒着计算到当前位置买卖股票的最大利润
            result = resultafter[j] = max(result, end - prices[j])  # 计算存储最大利润
            end = max(end, prices[j])                               # 更新卖出价格

        rel = 0  # 用来记录最终的最大利润
        for i in range(len(prices)):  # i为两次交易的分界线，遍历列表，记录不同分界线情况下两次交易的最终利润
            rel = max(rel, resultfront[i] + resultafter[i])   # 取利润最大值
        return rel

# nums = [3,3,5,0,0,3,1,4]
# nums = [1,2,3,4,5]
nums = [1,2,4,2,5,7,2,4,9,0]
S = Solution()
a = S.maxProfit(nums)
print(a)