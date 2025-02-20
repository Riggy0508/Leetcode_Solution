// https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', val: int) -> 'Node':
        new_node=Node(val)

        if not head:
            new_node.next=new_node
            return new_node
        
        current=head
        while True:
            next_node=current.next

            if current.val<=val<=next_node.val:
                break

            if current.val > next_node.val:
                if val>=current.val or val<=next_node.val:
                    break

            current=next_node

            if current==head:
                break
        current.next=new_node
        new_node.next=next_node

    
        return head
