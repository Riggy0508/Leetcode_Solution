// https://leetcode.com/problems/linked-list-cycle

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        slow,fast=head,head.next
        
        while fast is not None or fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            
            if slow.val==fast.val:
                return True
            
        return False