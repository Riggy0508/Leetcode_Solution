// https://leetcode.com/problems/cousins-in-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.is_Cousins=False
        self.recorded_depth=None
        
    def dfs(self,root,depth,x,y):
        
        if root is None:
            return False
        
        if self.recorded_depth and depth>self.recorded_depth:
            return False
        
        if root.val==x or root.val==y:
            if self.recorded_depth is None:
                self.recorded_depth=depth
            return self.recorded_depth==depth
        
        left=self.dfs(root.left,depth+1,x,y)
        right=self.dfs(root.right,depth+1,x,y)
        
        if left and right and self.recorded_depth!=depth+1:
            self.is_Cousins=True
            
        return left or right
        
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.dfs(root,0,x,y)
        return self.is_Cousins