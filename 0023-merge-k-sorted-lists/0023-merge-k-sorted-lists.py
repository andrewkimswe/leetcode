# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []

        for i, node in enumerate(lists):
            if node:
                heappush(min_heap, (node.val, i, node))

        dummy = ListNode()
        current = dummy

        while min_heap:
            val, i, node = heappop(min_heap)
            current.next = node
            current = current.next

            if node.next:
                heappush(min_heap, (node.next.val, i, node.next))

        return dummy.next