class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        
        ans, preidx = values[0], 0
        
        for j in range(1, len(values)):
            ans = max(ans, values[preidx] + preidx + values[j] - j)
            
            if values[preidx] + preidx < j + values[j]:
                preidx = j
                
        return ans