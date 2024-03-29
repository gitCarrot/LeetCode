# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        max_path = -987654321
        def solve(node):
            nonlocal max_path
            if not node: return 0
            
            left = max(solve(node.left), 0)
            right = max(solve(node.right), 0)
            
            cur_max_path = left + right + node.val
            max_path = max(max_path, cur_max_path)
            return node.val + max(left, right)
        
        solve(root)
        return max_path
            
        
        
        