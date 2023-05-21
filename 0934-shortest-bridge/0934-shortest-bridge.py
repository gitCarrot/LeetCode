class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        
        n = len(grid)
        visited = [[0] * (n) for _ in range(n)]
        ans = 987654321
        def bfs(i,j):
            nonlocal ans
            q = deque()
            q2 = deque()
            q.append((i,j,0,0))
            q2.append((i,j,0,0))
            visited[i][j] = 1           
            while q:
                cr, cc, dist, cs = q.popleft()
                for dr, dc in ((-1,0), (1, 0), (0, 1), (0, -1)):
                    nr, nc = cr + dr, cc + dc
                    if nr < 0 or nc < 0 or nr >= n or nc >= n: continue
                    if visited[nr][nc]: continue
                    if grid[nr][nc] == 1:
                        visited[nr][nc] = 1
                        q.append((nr,nc,0,0))
                        q2.append((nr,nc,0,0))
            print(q2)
                        
            while q2:
                cr, cc, dist, cs = q2.popleft()
                if grid[cr][cc] == 1 and cs == 1:
                    ans = min(ans, dist-1)
                for dr, dc in ((-1,0), (1, 0), (0, 1), (0, -1)):
                    nr, nc = cr + dr, cc + dc
                    if nr < 0 or nc < 0 or nr >= n or nc >= n: continue
                    if visited[nr][nc]: continue
                    if grid[nr][nc] == 0:
                        visited[nr][nc] = 1
                        q2.append((nr,nc,dist+1, 1))
                    else:
                        visited[nr][nc] = 1
                        q2.append((nr,nc,dist+1, 1))
                        
                        
            
                    
                    
                        
                        
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    bfs(i,j)
                    return ans
                    
        
        
        
        