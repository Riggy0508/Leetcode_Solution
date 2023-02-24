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
        oldToNew={}
        
        def dfs(root):
            if root in oldToNew:
                return oldToNew[root]
            
            copy=Node(root.val)
            oldToNew[root]=copy
            
            for n in root.neighbors:
                copy.neighbors.append(dfs(n))
            
            return copy
            
            
            
            
        return dfs(node) if node else None
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        oldToNew={}
        def dfs(root):
            
            if root in oldToNew:
                return oldToNew[root]
            
            copy=Node(root.val)
            oldToNew[root]=copy
            
            for n in root.neighbors:
                copy.neighbors.append(dfs(n))
            
            return copy

        return dfs(node) if node else None