class Solution:
    def fib(self, n: int) -> int:
        
        @lru_cache(None)
        def getfib(num):
            if num == 1: return 1
            if num == 0: return 0
            return getfib(num-1) + getfib(num-2)
        
        return getfib(n)
        
        