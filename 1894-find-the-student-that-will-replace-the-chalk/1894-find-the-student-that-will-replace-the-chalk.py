class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        
        total = 0
        for i in chalk:
            total += i
            
        idx = 0
        
        if total <= k:
            k %= total
        
        for i in chalk:
            k -= i
            if k < 0:
                return idx
            else:
                idx += 1
        
        return 0
            
            
        
            
        
            
        