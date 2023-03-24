from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_val = float("inf")
        result = 0

        for price in prices:
            
            if price < min_val:
                min_val = price
            elif price - min_val > result:
                result = price - min_val
        return result


if __name__ == '__main__':

    sol = Solution()
    prices = [7,1,5,3,6,4]
    print(sol.maxProfit(prices))