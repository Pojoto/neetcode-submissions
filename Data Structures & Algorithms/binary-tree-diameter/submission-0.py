# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def discover(self, root):

        left_sum = 0
        left_bent = 0
        if root.left:
            left_straight, left_bent = self.discover(root.left)
            left_sum = 1 + left_straight
        right_sum = 0
        right_bent = 0
        if root.right:
            right_straight, right_bent = self.discover(root.right)
            right_sum = 1 + right_straight

        max_straight = max(left_sum, right_sum)
        max_bent = max((left_sum + right_sum), left_bent, right_bent)
        
        return max_straight, max_bent

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        max_straight, max_bent = self.discover(root)

        return max(max_straight, max_bent)
    

