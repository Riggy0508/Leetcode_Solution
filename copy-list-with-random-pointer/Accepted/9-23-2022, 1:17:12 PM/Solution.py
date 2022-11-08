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
        
        #here we will be makine use of 2 pass algorithm
        
        #first we will copy the node in our hashmap and in the second pass we will make connection's/link between each node
        
        #first pass
        oldCopy={None:None}
        cur=head
        while cur:
            copy=Node(cur.val)
            oldCopy[cur]=copy
            cur=cur.next
            
        cur=head
        while cur:
            copy=oldCopy[cur]
            copy.next=oldCopy[cur.next]
            copy.random=oldCopy[cur.random]
            cur=cur.next
            
        return oldCopy[head]
            