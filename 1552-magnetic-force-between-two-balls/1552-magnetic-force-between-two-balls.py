class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        
        l, r = 1, 1000000000
        ans = -1
        
        def check(c):
            cur, choose = position[0],1
            for i in range(1, len(position)):
                if position[i] - cur >= c:
                    choose += 1
                    cur = position[i]
            if choose >= m:
                return True
            else:
                return False
                
            
        
        while l <= r:
            mid = (l + r) // 2
            
            if check(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        
        return ans