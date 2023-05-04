class Solution:
    def jump(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        
        @lru_cache(None)
        def solve(idx):
            if idx >= n: return 10000000
            if idx == n-1: return 0
            ans = 10000000
            if nums[idx] != 0:
                for i in range(idx+1, min(n, idx+nums[idx] + 1) ):
                    ans = min(ans, solve(i) + 1)
            return ans
        
        return solve(0)
        