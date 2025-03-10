// https://leetcode.com/problems/remove-nth-node-from-end-of-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return  
        temp=head
        length=0
        
        
        while temp:
            length+=1
            temp=temp.next
            
        pos_del=length-n
        
        if pos_del==0:
            head=head.next
            return head
        temp=head
        for _ in range(1,pos_del):
            temp=temp.next
        
        temp.next=temp.next.next
        return head