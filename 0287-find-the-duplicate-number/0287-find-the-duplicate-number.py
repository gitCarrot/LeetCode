class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        dic = defaultdict(int)
        
        for num in nums:
            if dic[num] == 1:
                return num
            else:
                dic[num] = 1
                
        
        return 0
        