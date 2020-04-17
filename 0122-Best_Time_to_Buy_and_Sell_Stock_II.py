'''
Difficulty: Easy

Say you have an array prices for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.


Constraints:

1 <= prices.length <= 3 * 10 ^ 4
0 <= prices[i] <= 10 ^ 4
'''
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lenp = len(prices)
        if lenp <= 1:
            return 0

        decrease = None
        increase = None
        bought = False
        curr_price = prices[0]
        bought_price = 0
        total = 0

        for i, x in enumerate(prices[1:]):
            if x < curr_price:  # Prices are starting to go down
                # print('d', x, curr_price, i, curr_price, decrease, increase, bought, bought_price, total, lenp)
                if increase:  # If transitioning from going up to going down, sell
                    if bought:
                        total += (curr_price - bought_price)
                        curr_price = x
                        bought_price = -1
                        bought = False
                curr_price = x
                decrease = True
                increase = False
            elif x > curr_price:  # Prices are starting to go up
                # print('i', x, curr_price, i, curr_price, decrease, increase, bought, bought_price, total, lenp)
                decrease = False
                increase = True
                if increase:
                    if not bought:  # If transitioning from going down to up, buy
                        bought = True
                        bought_price = curr_price
                curr_price = x
                if i == lenp - 2:
                    total += (x - bought_price)
                    # print('int this look', x, bought_price)

            else:
                if i == lenp - 2 and increase:
                    total += (x - bought_price)
            # print(total)

        return total