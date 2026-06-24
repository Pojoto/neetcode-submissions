# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        
        node_stack = []
        heights = {}

        node_stack.append((root, False))

        while len(node_stack) > 0:
            
            node_tuple = node_stack.pop()
            node = node_tuple[0]
            visited = node_tuple[1]

            if visited:
                left_height = heights.get(node.left, 0)
                right_height = heights.get(node.right, 0)

                heights[node] = 1 + max(left_height, right_height)

                if abs(left_height - right_height) > 1:
                    return False
            else:
                node_stack.append((node, True))
                if node.left:
                    node_stack.append((node.left, False))
                if node.right:
                    node_stack.append((node.right, False))
            
        return True

            