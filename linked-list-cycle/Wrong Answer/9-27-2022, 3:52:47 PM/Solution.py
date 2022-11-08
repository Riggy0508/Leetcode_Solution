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
        
        while fast is not None and fast.next is not None:
            if slow!=fast:
                slow=slow.next
                fast=fast.next.next
            return True
            
        return False