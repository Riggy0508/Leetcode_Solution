// https://leetcode.com/problems/remove-nth-node-from-end-of-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        temp=head
        lenght=0
        
        while temp:
            lenght+=1
            temp=temp.next
            
        pos_del=lenght-n
        
        if pos_del==0:
            head=head.next
            return head
        prev=head
        for _ in range(1,pos_del):
            prev=prev.next
        prev.next=prev.next.next
        return head
        