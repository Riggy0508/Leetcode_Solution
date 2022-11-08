// https://leetcode.com/problems/palindrome-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head.next
        
        #find middle
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            
        
        #Reverse the second half
        second=slow.next
        prev=slow.next=None
        
        while second:
            temp=second.next
            second.next=prev
            prev=second
            second=temp
            
            
        #check if palindrone or not
        first=head
        second=prev
        while second:
            if first.val!=second.val:
                return False
            first=first.next
            second=second.next
        return True