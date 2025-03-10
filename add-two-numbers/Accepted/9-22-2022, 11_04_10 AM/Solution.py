// https://leetcode.com/problems/add-two-numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        cur=dummy
        carry=0
        
        
        while l1 or l2 or carry:
            #here we are storing the linked list value in order to perform addition later one
            v1=l1.val if l1 else 0
            v2=l2.val if l2 else 0
            
            #once we have independent value we will perform the addition
            val=v1+v2+carry
            #checking if the number if greater then 10
            carry=val//10
            val=val%10
            #appending the value in the linked list and creating a link between dummy and the new node
            cur.next=ListNode(val)
            
            #print(cur)
            
            #updating the pointers
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
            cur=cur.next
            
        return dummy.next
            
            