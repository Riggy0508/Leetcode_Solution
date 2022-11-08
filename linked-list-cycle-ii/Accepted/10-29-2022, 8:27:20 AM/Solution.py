// https://leetcode.com/problems/linked-list-cycle-ii

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        
        slow=head
        fast=head
        
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                break

        #print(slow)
        
        slow2=head
        
        while slow.next:
            if slow2==slow:
                return slow2
            slow=slow.next
            slow2=slow2.next
            
        return