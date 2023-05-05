class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        ans, l = 10000000, 0
        total = 0
        for r in range(len(nums)):
            total += nums[r]
            
            while total >= target:
                ans = min(ans, r - l + 1)
                total -= nums[l]
                l +=1
                
        return ans if ans != 10000000 else 0
                
            
        