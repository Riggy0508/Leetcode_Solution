// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii

"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        visited=set()

        while p:
            visited.add(p)
            p=p.parent

        while q:
            if q in visited:
                return q
            q=q.parent

            
