// https://leetcode.com/problems/linked-list-cycle-ii

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return
        
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if fast==slow:
                break
                
        else:
            return None
        
        
        s2=head
        while slow!=s2:
            slow=slow.next
            s2=s2.next
        return s2
            