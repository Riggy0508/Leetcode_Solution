// https://leetcode.com/problems/reverse-linked-list-ii

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummyNode=ListNode()
        dummyNode.next=head
        
        lp=dummyNode
        curr=head
        
        #Traversing till the left point
        for i in range(left-1):
            curr=curr.next
            lp=lp.next
            
            
        #Reversing the range of our linked list
        prev=None
        for i in range(right-left+1):
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        
        #Considering the example 1. Creating the link's between Node 1 and Node 4 +  Node 2 and Node 5
        #Before going ahead one should notice that now, our current is pointing towards 5 & our lp is pointing at 1 & prev is pointing at 4
        
        lp.next.next=curr
        lp.next=prev
        
        return dummyNode.next