# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0
        
        max_depth = 0
        node_stack = []
        node_stack.append((root, 1))

        while len(node_stack) > 0:
            current_node = node_stack.pop()
            depth = current_node[1]
            node = current_node[0]
            
            if depth > max_depth:
                max_depth = depth
            
            if node.left:
                node_stack.append((node.left, depth + 1))
            if node.right:
                node_stack.append((node.right, depth + 1))


        return max_depth