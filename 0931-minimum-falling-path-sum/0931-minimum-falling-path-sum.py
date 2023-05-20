class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        
        n = len(matrix)
        
        @lru_cache(None)
        def solve(row, col):
            if row == n:
                return 0
            minValue = min(solve(row+1, max(col-1, 0)), solve(row+1, min(col+1, n-1)), solve(row+1, col))
            
            return matrix[row][col] + minValue
        ans = 987654321
        for i in range(n):
            ans = min(ans, solve(0,i))
            
        
        return ans
            