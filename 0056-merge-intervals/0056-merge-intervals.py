class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        ans = []
        ans.append(intervals[0])
        
        for st, ed in intervals[1:]:
            lastEnd = ans[-1][1]
            
            if st <= lastEnd:
                ans[-1][1] = max(lastEnd, ed)
            else:
                ans.append([st, ed])
                
        return ans
        
        
        
        