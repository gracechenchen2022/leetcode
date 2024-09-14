# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
from typing import List, Optional



class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 定义一个最小堆
        heap = []
        
        # 将每个链表的头节点（如果非空）压入堆
        for i, lst in enumerate(lists):
            if lst:  # 避免空链表
                heapq.heappush(heap, (lst.val, i, lst))  # 使用(i, lst)的索引i来避免同值节点的混淆
        
        # 定义一个虚拟头节点，方便处理链表
        dummy = ListNode()
        current = dummy
        
        # 不断从堆中取出最小的节点，并将其加入结果链表
        while heap:
            # 弹出堆顶的最小值
            val, i, node = heapq.heappop(heap)
            # 将该节点接到结果链表的末尾
            current.next = node
            current = current.next
            
            # 如果该节点有下一个节点，将下一个节点也压入堆中
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        
        # 返回合并后的链表
        return dummy.next
