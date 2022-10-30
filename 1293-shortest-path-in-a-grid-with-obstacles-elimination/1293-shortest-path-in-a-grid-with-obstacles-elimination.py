class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        visited = [[[0 for _ in range(k+1)]for _ in range(m)]for _ in range(n)]
        q = deque(); q.append((0,0,0)); visited[0][0][0]
        step = 0
        
        while q:
            qsize = len(q)
            while qsize:
                qsize -= 1
                cr,cc,ck = q.popleft()
                
                if cr == n-1 and cc == m-1:
                    return step
                
                for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    nr, nc = cr + dr, cc + dc
                    if 0<= nr < n and 0<= nc < m:
                        if grid[nr][nc] == 0 and not visited[nr][nc][ck]:
                            q.append((nr,nc,ck))
                            visited[nr][nc][ck] = True
                        else :
                            if ck+1 <= k and not visited[nr][nc][ck+1]:
                                q.append((nr,nc,ck+1))
                                visited[nr][nc][ck+1] = True
            step+=1                
        
        return -1;
        