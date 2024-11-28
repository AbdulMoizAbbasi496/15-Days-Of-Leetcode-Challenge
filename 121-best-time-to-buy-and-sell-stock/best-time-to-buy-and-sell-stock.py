class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    
        min_price = float('inf')  # Initialize to infinity
        max_profit = 0           # Initialize maximum profit to 0

        for price in prices:
            if price < min_price:
                min_price = price  # Update minimum price
            else:
                max_profit = max(max_profit, price - min_price)  # Calculate profit

        return max_profit

            