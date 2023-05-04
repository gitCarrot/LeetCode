class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curMax, totalMax = nums[0], nums[0]
        for i in nums[1:]:
            curMax = max(i, curMax + i)
            totalMax = max(totalMax, curMax)
            
        return totalMax
        