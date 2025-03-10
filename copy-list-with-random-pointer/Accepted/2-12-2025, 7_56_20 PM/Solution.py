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
        oldToNew={None:None}
        cur=head

        while cur:
            node=Node(cur.val)
            oldToNew[cur]=node
            cur=cur.next


        cur=head
        while cur:
            node=oldToNew[cur]
            node.next=oldToNew[cur.next]
            node.random=oldToNew[cur.random]
            cur=cur.next

        return oldToNew[head]