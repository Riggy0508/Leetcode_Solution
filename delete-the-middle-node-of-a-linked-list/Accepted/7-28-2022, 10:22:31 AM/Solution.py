// https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(next=head)
        slow,fast=head,head
        
        
        if not head.next:
            return None
        
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            
        node=head
        
        while node:
            if node.next==slow:
                node.next=node.next.next
            else:
                node=node.next
                
        return dummy.next