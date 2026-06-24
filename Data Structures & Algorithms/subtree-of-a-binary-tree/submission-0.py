# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        

        node_queue1 = deque()
        node_queue2 = deque()

        node_queue1.append(p)
        node_queue2.append(q)

        while len(node_queue1) > 0:

            node1 = node_queue1.popleft()
            node2 = node_queue2.popleft()

            if (node1 is None) and (node2 is None):
                continue
            elif (node1 is None) or (node2 is None):
                return False
            else:
                if node1.val != node2.val:
                    return False
                node_queue1.append(node1.left)
                node_queue1.append(node1.right)
                node_queue2.append(node2.left)
                node_queue2.append(node2.right)
        
        return True

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if root is None:
            return False

        is_subtree = self.isSameTree(subRoot, root)
        
        return ((is_subtree) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
    

