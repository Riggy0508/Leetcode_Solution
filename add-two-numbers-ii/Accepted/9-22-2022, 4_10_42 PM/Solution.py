// https://leetcode.com/problems/add-two-numbers-ii

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def reverse(self,l1):
        prev=None
        dummy=ListNode()
        cur=l1
        
        while cur:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
        return prev
    
    def add(self,l1,l2):
        carry=0
        dummy=ListNode
        cur=dummy
        while l1 or l2 or carry:
            v1=l1.val if l1 else 0
            v2=l2.val if l2 else 0
            
            val=v1+v2+carry
            carry=val//10
            val=val%10
            cur.next=ListNode(val)
            
            cur=cur.next
            l1=l1.next if l1 else 0  
            l2=l2.next if l2 else 0
            
        return dummy.next
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1=self.reverse(l1)
        l2=self.reverse(l2)
        
        ans=self.add(l1,l2)
        
        res=self.reverse(ans)
        
        return res
        