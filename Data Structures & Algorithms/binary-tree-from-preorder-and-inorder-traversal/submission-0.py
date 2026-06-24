# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        visited = {}
        
        preorder_i = 0
        inorder_i = 0

        while inorder_i < len(inorder) and preorder_i < len(preorder):

            incline_start_i = preorder_i
            current_inorder_val = inorder[inorder_i]
            
            dont_break = True
            while dont_break:
                current_preorder_val = preorder[preorder_i]
                new_node = TreeNode(current_preorder_val)
                visited[current_preorder_val] = new_node
                if preorder_i - 1 >= incline_start_i:
                    visited[preorder[preorder_i - 1]].left = new_node
                
                if current_preorder_val == current_inorder_val:
                    dont_break = False

                preorder_i += 1

            if inorder_i - 1 >= 0:
                visited[inorder[inorder_i - 1]].right = visited[preorder[incline_start_i]]
            
            while inorder_i < len(inorder) and visited.get(inorder[inorder_i], False):
                inorder_i += 1
                
        
        return visited[preorder[0]]


