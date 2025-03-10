// https://leetcode.com/problems/clone-graph

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        #We are maintaining a hashmap to map all the old node's to there new node(essentially Copy)
        oldToNew={}
        
        def dfs(root):
            #We are gonna check if this root is already present in our hashmap if yes, we will return it's value
            if root in oldToNew:
                return oldToNew[root]
            
            #if the root is not present in the hashmap we will create a copy of it and add it into the hashmap.
            copy=Node(root.val)
            oldToNew[root]=copy
            
            #Once done with that we are gonna check with the root's neighbor's
            for n in root.neighbors:
                #create a copy of this neighbors
                copy.neighbors.append(dfs(n))
                
            return copy

        return dfs(node) if node else None