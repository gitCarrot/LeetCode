class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        
        dp = [0 for _ in range(high+1)]
        mod = 10**9+7
        
        dp[zero] = 1
        dp[one] += 1
        
        for i in range(high+1):
            
            if i-zero >= 0:
                dp[i] += dp[i-zero] % mod
                
            if i-one >= 0:
                dp[i] += dp[i-one] % mod
                
            
        return sum(dp[low:high+1]) % mod
        
                
        
            
            
        
        
        