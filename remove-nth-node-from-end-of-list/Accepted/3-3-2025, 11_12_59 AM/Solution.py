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

        fast=slow=dummyNode

        for _ in range(n+1):
            fast=fast.next

        while fast:
            slow=slow.next
            fast=fast.next

        slow.next=slow.next.next

        return dummyNode.next