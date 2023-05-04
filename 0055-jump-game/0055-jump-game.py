class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        @lru_cache(None)
        def canJump(idx):
            if idx == len(nums)-1: return True
            if nums[idx] != 0:
                for i in range(idx+1, min(idx+nums[idx]+1, len(nums))):
                    if canJump(i) : return True
            return False
        
        return canJump(0)
            
        