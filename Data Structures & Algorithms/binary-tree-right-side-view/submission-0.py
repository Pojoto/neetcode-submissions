# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if root is None:
            return []

        return_list = []
        
        node_queue = deque()
        node_queue.append(root)

        while len(node_queue) > 0:
            
            level_node_amount = len(node_queue)

            for i in range(level_node_amount):
                node = node_queue.popleft()
                if node.left:
                    node_queue.append(node.left)
                if node.right:
                    node_queue.append(node.right)
                
                if i == level_node_amount - 1:
                    return_list.append(node.val)
            
        
        return return_list
            
