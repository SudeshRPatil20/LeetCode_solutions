# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        current_node=head
        s=[]

        while current_node is not None:
            s.append(current_node.val)
            current_node= current_node.next
        
        while head is not None:
            current = s.pop()

            if head.val != current:
                return False
            
            head = head.next
        return True

