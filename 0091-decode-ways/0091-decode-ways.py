class Solution:
    def numDecodings(self, s: str) -> int:
        
        n = len(s)
        @lru_cache(None)
        def solve(idx):
            if idx >= n: return 1
            total = 0
            if s[idx] == '0':
                return 0
            else:
                total += solve(idx+1)
            
            if idx != n-1 and 10 <= int(s[idx:idx+2]) <= 26:
                total += solve(idx + 2)
                
            return total
        
        
        return solve(0)
        
        