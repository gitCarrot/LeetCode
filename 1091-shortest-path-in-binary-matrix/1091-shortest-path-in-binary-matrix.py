class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        if grid[0][0] == 1: return -1
        dp = [[-1 for _ in range(n)] for _ in range(n)]
        dp[0][0] = 1
        q = deque([(0, 0)])
        
        
        while q:
            
            cr, cc = q.popleft()
            
            if cr == n-1 and cc == n-1:
                break
            
            for nr, nc in ((cr-1, cc), (cr, cc-1), (cr+1, cc), (cr, cc+1), (cr+1,cc+1), (cr-1,cc-1), (cr-1,cc+1), (cr+1,cc-1)):
                if nr < 0 or nc < 0 or nr >=n or nc >= n: continue
                if dp[nr][nc] != -1 : continue
                if grid[nr][nc] == 1: continue
                
                dp[nr][nc] = dp[cr][cc] + 1
                q.append((nr,nc))
                
        return dp[n-1][n-1]
    