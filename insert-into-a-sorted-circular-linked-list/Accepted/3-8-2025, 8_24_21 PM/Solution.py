// https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':

        if not head:
            newNode=ListNode(insertVal)
            newNode.next=newNode
            return newNode
        
        isInsert=False
        prev,cur=head,head.next


        while True:

            if prev.val<=insertVal<=cur.val:
                isInsert=True
            
            if prev.val>cur.val:
                if insertVal>=prev.val or cur.val>=insertVal:
                    isInsert=True


            if isInsert:
                prev.next=ListNode(insertVal,cur)
                return head

            prev,cur=cur,cur.next

            if prev==head:
                break

        prev.next=ListNode(insertVal,cur)
        return head


            
