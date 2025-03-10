// https://leetcode.com/problems/remove-nth-node-from-end-of-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #First we are gonna point a node to the head in order to traverse the linked list
        temp=head
        #According to the logic that I have implemented I will first calculate the total length of the linked list and then sustract it from the given n in order to find the actual node that need's to be deleted.
        length=0
        
        #Traversing through the linked list in order to find the length untill temp is None
        while temp:
            length+=1
            temp=temp.next
            
        #Formula the calculate the actual node to be deleted
        pos_del=length-n
        
        #For an edge case, consider that we need to delete the head node then we will apply the following logic. Because there is only one position to delete according to the question we can immediately return the head.
        if pos_del==0:
            head=head.next
            return head
        #Now for all the other cases, we will traverse till the position to be deleted and then point the next to next.next. 
        #Because we have already taken care of the head i.e 0th postion we can traverse from 1.
        #we are using a new pointer (But don't worry it's all constant space)
        prev=head
        for _ in range(1,pos_del):
            prev=prev.next
            
        prev.next=prev.next.next
        return head
            
        