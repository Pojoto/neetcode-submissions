# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        balanced = True

        def max_height(root):

            nonlocal balanced

            if root is None or not balanced:
                return 0
            
            left_height = max_height(root.left)
            right_height = max_height(root.right)

            if abs(left_height - right_height) > 1:
                balanced = False
            
            return 1 + max(max_height(root.left), max_height(root.right))

        max_height(root)

        return balanced
