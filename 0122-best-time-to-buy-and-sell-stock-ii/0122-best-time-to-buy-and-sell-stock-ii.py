class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        @lru_cache(None)
        def maxProfit(idx, canBuy):
            if idx == len(prices): return 0
            return max(maxProfit(idx+1, 0) - prices[idx], maxProfit(idx+1, 1)) if canBuy else max(maxProfit(idx+1, 1) + prices[idx], maxProfit(idx+1, 0))
            
        return maxProfit(0, 1)
                
                
        