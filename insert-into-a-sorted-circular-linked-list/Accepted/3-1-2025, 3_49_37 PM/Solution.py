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
            newNode=Node(insertVal)
            newNode.next=newNode
            return newNode

        prev=head
        cur=head.next
        isInsert=False

        while True:
            if prev.val<=insertVal<=cur.val:
                isInsert=True

            if prev.val>cur.val:
                if insertVal>prev.val or cur.val>insertVal:
                    isInsert=True

            if isInsert:
                prev.next=Node(insertVal,cur)
                return head

            prev,cur=cur,cur.next

            if prev==head:
                break

        prev.next=Node(insertVal,cur)
        return head

            
        