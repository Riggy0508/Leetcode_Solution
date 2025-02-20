// https://leetcode.com/problems/sort-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        slow,fast=head,head.next

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        mid=slow.next
        slow.next=None

        left=self.sortList(head)
        right=self.sortList(mid)

        return self.merge(left,right)



    def merge(self,l1,l2):
        dummyNode=ListNode()
        prev=dummyNode

        while l1 and l2:
            if l1.val < l2.val:
                prev.next=l1
                l1=l1.next
            else:
                prev.next=l2
                l2=l2.next

            prev=prev.next

        if l1:
            prev.next=l1
        if l2:
            prev.next=l2

        return dummyNode.next