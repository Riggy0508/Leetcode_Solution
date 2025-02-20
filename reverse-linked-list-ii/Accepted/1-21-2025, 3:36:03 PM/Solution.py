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
        cur=head


        for i in range(left-1):
            lp=lp.next
            cur=cur.next

        prev=None
        for i in range(right-left+1):
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp

        
        lp.next.next=cur
        lp.next=prev

        return dummyNode.next