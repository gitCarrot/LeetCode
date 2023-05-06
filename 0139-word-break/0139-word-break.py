class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:\
        
        st = set(wordDict)
        @lru_cache(None)
        def solve(start):
            if start == len(s): return True
            
            for end in range(start + 1, len(s)+1):
                w = s[start:end]
                if w in wordDict and solve(end):
                    return True
            return False
        
        return solve(0)
                