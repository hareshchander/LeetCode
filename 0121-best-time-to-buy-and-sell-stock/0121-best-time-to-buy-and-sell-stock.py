class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0  # Buy day
        maxProfit = 0

        for right in range(1, len(prices)):  # Iterate over the prices
            if prices[right] > prices[left]:  # Valid profit opportunity
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            else:
                left = right  # Update left pointer to the new minimum price

        return maxProfit