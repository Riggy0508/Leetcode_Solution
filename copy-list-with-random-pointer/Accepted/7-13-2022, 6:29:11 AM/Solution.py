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
        oldC={None:None}
        
        cur=head
        while cur:
            copy=Node(cur.val)
            oldC[cur]=copy
            cur=cur.next
            
        cur=head
        while cur:
            copy=oldC[cur]
            copy.next=oldC[cur.next]
            copy.random=oldC[cur.random]
            cur=cur.next
        return oldC[head]