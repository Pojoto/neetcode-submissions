# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        p_stack = []
        q_stack = []

        p_stack.append(p)
        q_stack.append(q)

        while len(p_stack) > 0:

            p_node = p_stack.pop()
            q_node = q_stack.pop()

            if p_node is None and q_node is None:
                continue
            if p_node is None or q_node is None:
                return False
            if p_node.val != q_node.val:
                return False
            
            p_stack.extend([p_node.left, p_node.right])
            q_stack.extend([q_node.left, q_node.right])

        return len(p_stack) == len(q_stack)