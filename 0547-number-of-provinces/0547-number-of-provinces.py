class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * (n)
        ans = 0
        def dfs(n):
            visited[n] = True
            
            for nxt in range(len(isConnected[n])):
                if isConnected[n][nxt] == 0 : continue
                if nxt == n: continue
                if visited[nxt]: continue
                dfs(nxt)
                
        for i in range(n):
            if not visited[i]:
                dfs(i)
                ans += 1
            
        return ans
            
        