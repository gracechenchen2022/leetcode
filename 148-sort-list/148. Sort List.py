# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left,right)
    def merge(self, left: ListNode, right: ListNode):
            dummy = ListNode()
            tail = dummy
            while left and right:
                if left.val < right.val:
                    tail.next = left
                    left = left.next
                else:
                    tail.next = right 
                    right = right.next
                tail = tail.next
            tail.next= left if left else right
            return dummy.next    