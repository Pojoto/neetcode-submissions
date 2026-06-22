"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        old_node_map = {}
        new_node_list = []

        current_node = head

        current_index = 0
        while current_node is not None:

            old_node_map[current_node] = current_index
            
            new_node = Node(current_node.val)

            new_node_list.append(new_node)

            current_node = current_node.next
            current_index += 1

        
        current_node = head
        current_index = 0
        while current_node is not None:
            next_node_index = old_node_map.get(current_node.next)
            random_node_index = old_node_map.get(current_node.random)
            new_node_list[current_index].next = new_node_list[next_node_index] if next_node_index is not None else None
            new_node_list[current_index].random = new_node_list[random_node_index] if random_node_index is not None else None
            current_node = current_node.next
            current_index += 1
        
        return new_node_list[0] if new_node_list else None
        
