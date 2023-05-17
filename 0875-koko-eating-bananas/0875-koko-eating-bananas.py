class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        
        
        l, r = 1, 1000000000
        ans = -1
        
        def check(c):
            hours = 0
            for i in piles:
                hours += ((i + c -1) // c)
            
            if hours > h:
                return False
            else: return True
            
        
        
        while l <= r:
            mid = (l+r)//2
            
            if check(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
                
                
        return ans
        