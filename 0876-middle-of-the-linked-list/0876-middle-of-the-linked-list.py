# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0

        headd = head

        while head:
            length += 1
            head = head.next
        
        midIndex =length // 2
        while midIndex:
            headd = headd.next
            midIndex -= 1
        
        return headd