// https://leetcode.com/problems/cousins-in-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#There are 2 conditions that we need to take care of
    #1. Same depth
    #2. Different Parent
class Solution:
    def __init__(self):
        self.is_Cousins=False
        self.recorded_depth=None
        
    def dfs(self,root,depth,x,y):
        #Base Condition
        if root is None:
            return False
        
        #Making sure that we are not traversing more than the depth of the other cousin if we have already found the depth of one.
        if self.recorded_depth and depth>self.recorded_depth:
            return False
        
        #in case if we are at the same depth
        # Checking for first conditio
        if root.val==x or root.val==y:  #Using OR instead of AND because we have make this program run for 2 cousin's 
            
            #Check if recored_depth is present for a condition so that we can now check for the other cousin 
            if self.recorded_depth is None:
                self.recorded_depth=depth
                
            #If the above is not None and both the depth's are same return True
            return self.recorded_depth==depth
            #Checking for second condition start's here and in case if we don't find the cousin's we keep on recursively do the same thing
        left=self.dfs(root.left,depth+1,x,y)
        right=self.dfs(root.right,depth+1,x,y)
        
        if left and right and self.recorded_depth!=depth+1:
            self.is_Cousins=True
            
        return left or right
        
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.dfs(root,0,x,y)
        return self.is_Cousins