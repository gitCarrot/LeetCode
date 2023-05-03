class Solution:
    def rob(self, nums: List[int]) -> int:
        
        @lru_cache(None)
        def solvelast(n):
            if n >= len(nums): return 0
            return max(nums[n] + solvelast(n+2), solvelast(n+1))
        
        @lru_cache(None)
        def solvefirst(n):
            if n >= len(nums)-1: return 0
            return max(nums[n] + solvefirst(n+2), solvefirst(n+1))
        
        return max(solvefirst(0), solvelast(1), nums[0])
        