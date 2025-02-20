// https://leetcode.com/problems/reorder-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow,fast=head,head
        
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            
        
        prev,cur=None,slow.next
        slow.next=None
        
        while cur:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
        
        first,second=head,prev
        while second:
            temp1,temp2=first.next,second.next
            first.next=second
            second.next=temp1
            first,second=temp1,temp2
        
        return head