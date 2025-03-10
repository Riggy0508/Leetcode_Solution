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
        if head==None:
            newNode=Node(insertVal,None)
            newNode.next=newNode
            return newNode

        prev,curr=head,head.next
        insert=False
        

        while True:
            if prev.val<=insertVal<=curr.val:
                insert=True
            elif prev.val>curr.val:
                if insertVal>=prev.val or insertVal<=curr.val:
                    insert=True
            
            if insert:
                prev.next=Node(insertVal,curr)
                return head
    
            if prev==head:
                break
        
        prev.next=Node(insertVal,curr)
        return head