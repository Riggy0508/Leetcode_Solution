// https://leetcode.com/problems/clone-graph

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        cloneGraph={}
        def bfs(root):
            if root in cloneGraph:
                return cloneGraph[root]
            
            new_node=Node(root.val)
            cloneGraph[root]=new_node

            for neigh in root.neighbors:
                new_node.neighbors.append(bfs(neigh))

            return new_node

        return bfs(node)