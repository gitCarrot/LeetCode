class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        n = len(intervals)
        ans = []
        for i in range(n):
            st, ed = intervals[i]
            
            if newInterval[1] < st:
                ans.append(newInterval)
                return ans + intervals[i:]
            elif ed < newInterval[0]:
                ans.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], st), max(newInterval[1], ed)]
        ans.append(newInterval)
        
        return ans
                