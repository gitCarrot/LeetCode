class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        neg, pos = 0, 0
        if nums[0] > 0 : pos = pos + 1
        if nums[0] < 0 : neg = neg + 1
        ans = pos
            
        for i in range(1, n):
            
            if nums[i] > 0:
                neg = neg + 1 if neg > 0 else 0
                pos = pos + 1
                
            elif nums[i] < 0:
                neg, pos = pos + 1, neg + 1 if neg > 0 else 0
            else:
                neg, pos = 0, 0
                
            ans = max(ans, pos)
        
        
        return ans
        
            
            
            
        