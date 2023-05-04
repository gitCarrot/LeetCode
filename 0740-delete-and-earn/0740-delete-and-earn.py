class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums.sort()
        counter = Counter(nums)
        st = list(set(nums))
        n = len(counter.keys())
        @lru_cache(None)
        def solve(idx):
            if idx >= n: return 0
            if idx + 1 < n:
                if st[idx+1] - st[idx] > 1 : return solve(idx+1) + st[idx] * counter[st[idx]]
            return max(solve(idx + 2) + st[idx] * counter[st[idx]], solve(idx+1))
        
        return solve(0)