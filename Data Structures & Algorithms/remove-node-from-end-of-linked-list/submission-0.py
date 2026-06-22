# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 1
        current_node = head
        while current_node.next != None:
            length += 1
            current_node = current_node.next
        
        dummy_node = ListNode(0, head)
        current_node = dummy_node
        current_index = 0

        while current_index < length - n:
            current_node = current_node.next
            current_index += 1

        current_node.next = current_node.next.next

        return dummy_node.next