# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        return_string = ""

        node_queue = deque()
        node_queue.append(root)
        next_level_good = True
        while len(node_queue) > 0 and next_level_good:

            level_amount = len(node_queue)

            next_level_good = False
            for i in range(level_amount):
                node = node_queue.popleft()

                if node is None:
                    return_string += "#|"
                    continue
                return_string += (str(node.val) + "|")
                    
                if node.left is not None or node.right is not None:
                    next_level_good = True
                node_queue.append(node.left)
                node_queue.append(node.right)
        
        return return_string[:-1]
        


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        strings = data.split("|")

        string_i = 0

        string_one = strings[string_i]
        if string_one == "#":
            return None
        

        node_queue = deque()

        root_node = TreeNode(int(string_one))
        node_queue.append(root_node)

        string_i += 1

        while len(node_queue) > 0 and string_i < len(strings):
            node = node_queue.popleft()

            left_node = None
            if strings[string_i] != "#":
                left_node = TreeNode(int(strings[string_i]))
                node_queue.append(left_node)


            node.left = left_node

            string_i += 1

            if string_i >= len(strings):
                break

            right_node = None
            if strings[string_i] != "#":
                right_node = TreeNode(int(strings[string_i]))
                node_queue.append(right_node)

            node.right = right_node

            string_i += 1

        return root_node


