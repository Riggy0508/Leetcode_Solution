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
        odlToNew={None:None}
        cur=head

        while cur:
            node=Node(cur.val)
            odlToNew[cur]=node
            cur=cur.next

        cur=head
        while cur:
            node=odlToNew[cur]
            node.next=odlToNew[cur.next]
            node.random=odlToNew[cur.random]
            cur=cur.next

        return odlToNew[head]