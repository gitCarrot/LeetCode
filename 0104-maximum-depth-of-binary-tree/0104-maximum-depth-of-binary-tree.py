# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        
        
        def maxdepth(node):
            return max(maxdepth(node.left), maxdepth(node.right)) + 1 if node else 0
        
        return maxdepth(root)
        