from typing import List


"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""

test_case = [7, 1, 5, 3, 6, 4]


# O(n^2) - brute force
def get_max_profit(prices: list) -> int:
    max_profit = 0
    for i in range(len(prices)):
        for x in range(len(prices)):
            if i >= x:
                continue
            profit = prices[x] - prices[i]
            if profit > max_profit:
                max_profit = profit

    return max_profit


# O(n)
def get_max_profit_faster(prices: list) -> int:
    buy = prices[0]
    max_profit = 0

    for i in range(1, len(prices)):
        profit = prices[i] - buy

        if profit > max_profit:
            max_profit = profit

        if buy > prices[i]:
            buy = prices[i]

    return max_profit


def test_get_max_profit():
    assert get_max_profit(test_case) == 5


def test_get_max_profit_faster():
    assert get_max_profit_faster(test_case) == 5

