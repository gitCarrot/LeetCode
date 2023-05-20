# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        
        def dfs(n):
            if not n: return 0
            left = dfs(n.left)
            right = dfs(n.right)
            
            if left == 0 or right == 0: return left + right + 1
            return min(left, right) + 1
                       
        return dfs(root)
        