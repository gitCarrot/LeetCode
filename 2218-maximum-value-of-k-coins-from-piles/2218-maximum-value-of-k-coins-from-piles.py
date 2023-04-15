class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        
        
        dp = [[0 for _ in range(k+1)] for _ in range(len(piles)+1)]
        
        
        
        for i in range(1, len(piles)+1):
            
            for j in range(1, k+1):
                
                cursum = 0
                
                for z in range(min(j, len(piles[i-1]))):
                    
                    cursum += piles[i-1][z]
                    
                    dp[i][j] = max(dp[i][j], cursum + dp[i-1][j-z-1])
                    
                
                dp[i][j] = max(dp[i][j], dp[i-1][j])
                
                
        return dp[len(piles)][k]
                