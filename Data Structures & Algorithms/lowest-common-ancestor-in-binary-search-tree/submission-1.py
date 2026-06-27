# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        

        lowest_node = root
        done = False

        def dfs(root):

            nonlocal lowest_node
            nonlocal done

            if root is None:
                return False, False, 0
            
            am_i_p = p.val == root.val
            am_i_q = q.val == root.val

            left_p, left_q, height = dfs(root.left)
            right_p, right_q, height = dfs(root.right)

            my_p = (left_p or right_p or am_i_p)
            my_q = (left_q or right_q or am_i_q)
            my_height = 1 + height

            if my_p and my_q and not done:
                lowest_node = root
                done = True
            return my_p, my_q, my_height
        
        dfs(root)
        return lowest_node
