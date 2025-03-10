// https://leetcode.com/problems/copy-list-with-random-pointer

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur=head

        oldToCopy={None:None}

        while cur:
            node=Node(cur.val)
            oldToCopy[cur]=node
            cur=cur.next
        
        cur=head
        while cur:
            node=oldToCopy[cur]
            node.next=oldToCopy[cur.next]
            node.random=oldToCopy[cur.random]
            cur=cur.next
        
        return oldToCopy[head]