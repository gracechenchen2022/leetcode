# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while head and head.next:
            # head.next = prev
            # head = head.next
            # prev. = head
            first_node = head
            second_node = head.next
            prev.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node
            prev = first_node
            head = first_node.next
        return dummy.next
