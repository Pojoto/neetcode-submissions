# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        return_list = ListNode()

        current_l1_node = l1
        current_l2_node = l2
        current_return_node = return_list
        carry = 0

        while current_l1_node is not None or current_l2_node is not None:
            
            l1_value = current_l1_node.val if current_l1_node else 0
            l2_value = current_l2_node.val if current_l2_node else 0

            sum = (l1_value + l2_value + carry)

            ones_digit = sum % 10
            carry = sum // 10
            
            current_return_node.next = ListNode(ones_digit)
            

            if current_l1_node is not None:
                current_l1_node = current_l1_node.next
            
            if current_l2_node is not None:
                current_l2_node = current_l2_node.next

            current_return_node = current_return_node.next
        
        if carry == 1:
            current_return_node.next = ListNode(1)
        
        return return_list.next
