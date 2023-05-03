class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        @lru_cache(None)
        def solve(cur):
            if cur >= len(cost): return 0
            return cost[cur] + min(solve(cur+1), solve(cur+2))
        
        return min(solve(0), solve(1))
        
        