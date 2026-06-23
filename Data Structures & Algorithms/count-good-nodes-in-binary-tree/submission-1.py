# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        good_nodes = 0
        node_stack = []
        node_stack.append((root, float('-inf')))

        while len(node_stack) > 0:
            node_tuple = node_stack.pop()
            node = node_tuple[0]
            greatest_encounter = node_tuple[1]

            if node.val >= greatest_encounter:
                good_nodes += 1

            new_greatest_encounter = max(greatest_encounter, node.val)
            if node.left:
                node_stack.append((node.left, new_greatest_encounter))
            if node.right:
                node_stack.append((node.right, new_greatest_encounter))
        
        return good_nodes
            
            