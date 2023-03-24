from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left = 0
        right = 1
        result = 0
        while right < len(prices):

            buy = prices[left]
            sell = prices[right]
            profit = sell - buy
            if profit <= 0:
                left = right
            else:
                result = max(result, profit)
            right += 1
        return result


if __name__ == '__main__':

    sol = Solution()
    prices = [7,1,5,3,6,4]
    print(sol.maxProfit(prices))