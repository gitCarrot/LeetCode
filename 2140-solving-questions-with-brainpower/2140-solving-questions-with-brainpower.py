class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        
        @lru_cache(None)
        def solve(idx):
            if idx >= len(questions): return 0
            return max(solve(idx+1), questions[idx][0] + solve(idx+questions[idx][1]+1))
                       
        return solve(0)
        