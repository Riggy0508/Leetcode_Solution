// https://leetcode.com/problems/remove-linked-list-elements

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        #Creating a dummyNode to make it easy for us to return the final linked list after all the operation's are been performed
        dummyNode=ListNode(0)
        #Pointing the dummy node to the head of the linked list(i.e creating a connection between dummyNode and the given list)
        dummyNode.next=head
        
        #Example 3: Suppose that we need to delete a value(7) from a linked list where all the node's have same value we will have to point the prev to the dummynode because if we point prev to dummynode.next(i.e head) we will end up returning the last 7. According to the example we wanna return an empty list in this case
        cur,prev=head,dummyNode
        
        while cur:
            #Checking if the value of the current node is the same as the value we wanna delete
            if cur.val==val:
                #pointing the prev node which in the start was pointing to the dummyNode(Note: The prev is pointing to the dummyNode and not the head of the linked list)
                prev.next=cur.next
            else:
                prev=cur
            #irrespective if we found a node to delete or not we are moving to the next node
            cur=cur.next
        
        return dummyNode.next