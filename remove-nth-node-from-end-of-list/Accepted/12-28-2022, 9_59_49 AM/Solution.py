// https://leetcode.com/problems/remove-nth-node-from-end-of-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode=ListNode()
        dummyNode.next=head

        right=head
        left=dummyNode

        while n>0:
            right=right.next
            n-=1

        while right:
            left=left.next
            right=right.next
        
        left.next=left.next.next

        return dummyNode.next
