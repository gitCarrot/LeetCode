class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        
        
        indeg = [0 for _ in range(n)]
        
        for f, s in edges:
            indeg[s] += 1
        ans = []
        for i in range(n):
            if indeg[i] == 0:
                ans.append(i)
                
        return ans