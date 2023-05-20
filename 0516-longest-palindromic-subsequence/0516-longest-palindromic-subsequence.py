class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        
        @lru_cache(None)
        def solve(l, r):
            if l > r : return 0
            if l == r : return 1
            if s[l] == s[r]:
                return 2 + solve(l+1, r-1)
            else:
                return max(solve(l+1, r), solve(l, r-1))
        
        return solve(0,len(s)-1)