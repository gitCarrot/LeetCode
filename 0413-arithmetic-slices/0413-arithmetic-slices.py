class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        prevdp, dp = 0,1
        ans = 0
        for i in range(2, n):
            if nums[i-1] - nums[i-2] == nums[i] - nums[i-1]:
                ans += dp
                dp += 1
            else:
                dp = 1
                
        return ans
                