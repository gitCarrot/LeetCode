class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        n = len(graph)
        colored = [0] * (n+1)
        
        
        def isPossible(node, col, state):
            if state[node] != 0:
                return (col == state[node])
            
            state[node] = col
            
            for nxt in graph[node]: 
                if not isPossible(nxt, -col, state):
                    return False
                
            return True
        
        for i in range(n):
            if colored[i] == 0 and not isPossible(i, 1, colored):
                return False
            
        return True
            
            
            
        