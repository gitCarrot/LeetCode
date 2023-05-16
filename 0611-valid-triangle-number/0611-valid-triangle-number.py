class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(n-1, 1, -1):
            l = 0
            r = i-1
            
            while l < r:
                if nums[i] >= nums[l] + nums[r]:
                    l += 1
                else:
                    ans += r- l
                    r -= 1
                    
        return ans
                    
        