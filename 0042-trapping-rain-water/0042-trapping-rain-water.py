class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        
        maxLeft = height[0]
        
        larr = [0] * n
        rarr = [0] * n
        
        for l in range(1, n):
            larr[l] = max(height[l-1], larr[l-1])
        
        for r in range(n-2, -1, -1):
            rarr[r] = max(height[r+1], rarr[r+1])
            
        
        total = 0
        for i in range(n):
            if height[i] >= larr[i] or height[i] >= rarr[i]: continue
            
            total += min(larr[i], rarr[i]) - height[i]
            
        return total
        
            
            
            
        