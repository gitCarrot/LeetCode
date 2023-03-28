class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        dp = [987654321] * 366
        daytype = [1, 7, 30]
        
        for i in range(0, days[0]+1):
            dp[i]  = 0
            if i == days[0]:
                dp[days[0]] = min(costs)
               
        
        for i in range(1, len(days)):
            
            for temp in range(days[i-1]+1, days[i]):
                dp[temp] = dp[days[i-1]]
        
            for c in range(0, 3):
                if days[i] - daytype[c] >= 0:
                    dp[days[i]] = min(dp[days[i]], dp[days[i] - daytype[c]] + costs[c])
                else:
                    dp[days[i]] = min(dp[days[i]], costs[c])
        
        
                    
        return dp[days[len(days)-1]]
                    
            
        
                
        
        