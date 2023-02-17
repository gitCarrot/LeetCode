# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        
        ans = 10e9
        prev = 10e9
         
        def dfs(cur):
            nonlocal ans, prev
            
            if cur.left : dfs(cur.left)
            ans = min(ans, abs(cur.val - prev))
            prev = cur.val
            if cur.right : dfs(cur.right)
            
        dfs(root)
        return ans
            
            
            
            
            
     
        