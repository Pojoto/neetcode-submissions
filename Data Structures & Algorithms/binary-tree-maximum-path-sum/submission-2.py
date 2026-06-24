# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        max_val = root.val


        def path_sum(root):
            nonlocal max_val

            if root is None:
                return 0

            
            left_max_sum = path_sum(root.left)
            right_max_sum = path_sum(root.right)

            bent_sum = left_max_sum + right_max_sum + root.val
            straight_sum = max(root.val + max(left_max_sum, right_max_sum), root.val)
            max_val = max(bent_sum, max_val, straight_sum)

            return straight_sum
        
        path_sum(root)

        return max_val
        





