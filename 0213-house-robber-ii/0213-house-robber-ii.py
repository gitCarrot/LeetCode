class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        
		# function when considering the first and neglecting last house
        @functools.lru_cache(None)
        def util1(i):
            if i >= n-1:
                return 0
			
            return max(nums[i] + util1(i+2), util1(i+1))
        
		# function when considering the last and neglecting first house
        @functools.lru_cache(None)
        def util2(i):
            if i >= n:
                return 0
            
            return max(nums[i] + util2(i+2), util2(i+1))
        
        return max(util1(0), util2(1), nums[0])
        