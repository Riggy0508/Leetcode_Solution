// https://leetcode.com/problems/merge-k-sorted-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists or len(lists)==0:
            return None
        
        while len(lists)>1:
            mergedList=[]
            
            for i in range(0,len(lists),2):
                list1=lists[i]
                list2=lists[i+1] if i+1<len(lists) else None
                mergedList.append(self.merge(list1,list2))
            lists=mergedList
        return lists[0]
    
    def merge(self,l1,l2):
        dummy=ListNode()
        prev=dummy
        
        while l1 and l2:
            if l1.val<=l2.val:
                prev.next=l1
                prev=prev.next
                l1=l1.next
            else:
                prev.next=l2
                prev=prev.next
                l2=l2.next
        if l1:
            prev.next=l1
        if l2:
            prev.next=l2
        return dummy.next