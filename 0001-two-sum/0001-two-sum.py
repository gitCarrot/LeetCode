class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dict = defaultdict(int)
        ans = []
        for i, num in enumerate(nums):
            
            if dict[target-num]:
                ans.append(dict[target-num]-1)
                ans.append(i)
                return ans
            else:
                dict[num] = i+1
                
        