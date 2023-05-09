class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        dp = [0] * n
        dp[0] = 1
        ugly = [1]
        a,b,c = 0,0,0
        
        for i in range(1, n):
            dp[i] = min(ugly[a] * 2, ugly[b] * 3, ugly[c] * 5)
            
            if dp[a] * 2 == dp[i] : a += 1
            if dp[b] * 3 == dp[i] : b += 1
            if dp[c] * 5 == dp[i] : c += 1
                
            ugly.append(dp[i])
        
        return dp[n-1]
        
        
        