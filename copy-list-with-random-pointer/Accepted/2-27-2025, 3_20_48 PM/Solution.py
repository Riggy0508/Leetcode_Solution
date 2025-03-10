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
        hash1={None:None}

        cur=head

        while cur:
            node=Node(cur.val)
            hash1[cur]=node
            cur=cur.next

        cur=head

        while cur:
            node=hash1[cur]
            node.next=hash1[cur.next]
            node.random=hash1[cur.random]
            cur=cur.next

        return hash1[head]
