// https://leetcode.com/problems/merge-two-sorted-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1=list1
        l2=list2
        
        dummyNode=ListNode()
        prevNode=dummyNode
        
        while l1 and l2:
            if l1.val<=l2.val:
                prevNode.next=l1
                prevNode=prevNode.next
                l1=l1.next
            else:
                prevNode.next=l2
                prevNode=prevNode.next
                l2=l2.next
                
        if l1:
            prevNode.next=l1
        if l2:
            prevNode.next=l2
            
        return dummyNode.next
       
        