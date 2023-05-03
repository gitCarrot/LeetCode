class Solution:
    def climbStairs(self, n: int) -> int:
        
        
        @lru_cache(None)
        def solve(m):
            if m == 1: return 1
            if m == 2: return 2
            
            return solve(m-1) + solve(m-2)
        
        return solve(n)
        