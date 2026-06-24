# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def inorder(root):

            if root is None:
                return []
            
            left_subtree_list = inorder(root.left)
            right_subtree_list = inorder(root.right)

            return left_subtree_list + [root.val] + right_subtree_list
        
        node_list = inorder(root)

        return node_list[k - 1]