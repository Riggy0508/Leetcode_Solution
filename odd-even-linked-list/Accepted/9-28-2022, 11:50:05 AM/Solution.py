// https://leetcode.com/problems/odd-even-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #checking if the linked list is emplty or not
        if not head:return None
        #creating our odd and even pointer
        odd=head
        even=head.next
        #keeping a note of even head because at the end we will need to point the end of the odd list to the even list. 
        evenhead=even
        while even and even.next:
            odd.next=even.next
            odd=odd.next
            even.next=odd.next
            even=even.next
        #once the while loop is completed it indicates that we have our odd list and even list so now we will point the end of odd list to the start of evenlist.
        odd.next=evenhead
        return head