# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if fast:
            slow = slow.next
            
        left, right = head, Solution.reverse(slow)

        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True

    
    def reverse(head: ListNode) -> ListNode:
        pre, cur = None, head

        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next

        return pre