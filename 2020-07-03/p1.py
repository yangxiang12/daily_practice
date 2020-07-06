#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/7/3 16:23 
# @Author : 杨翔
# @File : p1.py 

"""
给定不同面额的硬币 coins 和一个总金额 amount。
编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
如果没有任何一种硬币组合能组成总金额，返回 -1。
[1,2,5]
10
"""


class Solution:
    def coinChange(self, coins, amount):
        # @functools.lru_cache(amount)
        def dp(rem):
            # print(rem)
            if rem < 0: return -1
            if rem == 0: return 0
            mini = int(1e9)
            for coin in self.coins:
                res = dp(rem - coin)
                if res >= 0 and res < mini:
                    mini = res + 1
            return mini if mini < int(1e9) else -1

        self.coins = coins
        if amount < 1: return -1
        return dp(amount)


#
# s = Solution()
# print(s.coinChange([5, 2, 1], 12))


def coinChange(coins, amount):
    """
        1. dp问题: dp[i] = min(dp[i], dp[i-coins[j]] + 1)
            0 < i < amount + 1, dp[i]代表最小的次数.
            dp[i-coins[j]] + 1中, 1代表coins[j]满足为一次, dp[i-coins[j]]为剩余的次数
        2. dp[i]均初始化为amount + 1, 为了判断.
    """
    dp = [amount + 1 for _ in range(amount + 1)]
    dp[0] = 0
    # 到amount总金额(金额当索引)
    for i in range(1, amount + 1):
        for j in range(len(coins)):
            # 只有硬币小于当前金额, 才能进行递推
            if coins[j] <= i:
                # dp[i]要么等于自身(已经被计算过),
                # 要么等于coins[j](一次) + (i - coins[j])的次数
                dp[i] = min(dp[i], dp[i - coins[j]] + 1)
    return -1 if dp[amount] > amount else dp[amount]
