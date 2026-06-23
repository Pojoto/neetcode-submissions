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
        node_queue = deque()
        node_queue.append((root, 1))

        while node_queue:
            node_tuple = node_queue.popleft()
            node = node_tuple[0]
            depth = node_tuple[1]

            max_depth = max(depth, max_depth)

            if node.left:
                node_queue.append((node.left, depth + 1))
            if node.right:
                node_queue.append((node.right, depth + 1))

        return max_depth