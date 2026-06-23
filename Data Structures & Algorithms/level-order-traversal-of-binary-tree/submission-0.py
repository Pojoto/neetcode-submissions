# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return []
        
        node_queue = deque()
        node_queue.append((root, 0))

        current_level = 0

        return_list = [[]]

        while len(node_queue) > 0:

            node_tuple = node_queue.popleft()
            node = node_tuple[0]
            level = node_tuple[1]

            if level > current_level:
                current_level = level
                return_list.append([node.val])
            else:
                return_list[level].append(node.val)
            
            if node.left:
                node_queue.append((node.left, level + 1))
            if node.right:
                node_queue.append((node.right, level + 1))

        
        return return_list

