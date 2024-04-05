# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # 创建两个哑节点
        dummy1 = ListNode(0)
        dummy2 = ListNode(0)
        small = dummy1
        large = dummy2

        # 遍历原链表
        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                large.next = head
                large = large.next
            head = head.next

        # 将两个链表连接
        small.next = dummy2.next
        large.next = None  # 防止形成环

        return dummy1.next