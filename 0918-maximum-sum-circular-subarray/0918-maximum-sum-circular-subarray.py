class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        
        
        def kadein(arr):
            curMax, tMax = arr[0], arr[0]
            curMin, tMin = arr[0], arr[0]
            for i in arr[1:]:
                curMax = max(i, curMax + i)
                curMin = min(i, curMin + i)
                tMax = max(curMax, tMax)
                tMin = min(curMin, tMin)
            if sum(arr) == tMin : return tMax
            return max(tMax, sum(arr)-tMin)
        
        return kadein(nums)
            
            
        