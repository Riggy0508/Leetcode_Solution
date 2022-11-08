// https://leetcode.com/problems/maximum-depth-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #We know that the maximum depth of a root node is 0
        if root is None:
            return 0
        
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
    
    
    
    #In order to better understand this, let's solve an example.
    #For simplicity I will be use md for maxDepth
    #md(3)=max(md(9),md(20))+1
    #md(9)=max(md(leftnode which is none),md(rightNode which is none))+1, Therefore md(9)=max(md(0),md(0))+1
    #md(9)=1
    #md(20)=max(md(15),md(7))+1
    #md(15)=1   Just like 9
    #md(7)=1    Just like 9
    #md(20)=max(md(15),md(7))+1
        #= max(1,1)+1=2
    #now for md(3)=max(1,2)+1
        #=2+1
        #=3
    
    
    
    
        
        