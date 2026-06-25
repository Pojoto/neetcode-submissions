# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def r(root):

            if root is None:
                return True, 0

            left_bool, left_height = r(root.left)
            right_bool, right_height = r(root.right)

            balanced = left_bool and right_bool and (abs(left_height - right_height) <= 1)

            return balanced, 1 + max(left_height, right_height)
        
        return r(root)[0]

