"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        visited = {}
        
        def dfs(curNode):
            
            if not curNode: return None
            if curNode in visited: return visited[curNode]
            
            newGraph = Node(curNode.val)
            visited[curNode] = newGraph
            
            for nxt in curNode.neighbors:
                newGraph.neighbors.append(dfs(nxt))
                
            return newGraph
        
        return dfs(node)
            
        
        