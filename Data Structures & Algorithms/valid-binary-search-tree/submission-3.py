# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def bst_recurse(root, lower, upper):
            if root is None:
                return True
            
            am_i_valid = False
            if root.val > lower and root.val < upper:
                am_i_valid = True

            return (am_i_valid and bst_recurse(root.left, lower, root.val) and bst_recurse(root.right, root.val, upper))

        return bst_recurse(root, float('-inf'), float('inf'))
