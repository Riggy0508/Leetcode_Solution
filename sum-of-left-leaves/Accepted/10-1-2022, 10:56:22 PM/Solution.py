// https://leetcode.com/problems/sum-of-left-leaves

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#The main logic begin
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        #Checking if root is available if not we will return 0 immediately 
        if root is None:
            return 0
        
        def pro_subtree(node,is_left):
            if node.left is None and node.right is None:
                return node.val if is_left else 0
            
            total=0
            if node.left:
                total+=pro_subtree(node.left,True)
            if node.right:
                total+=pro_subtree(node.right,False)
            return total
            
        
        return pro_subtree(root,False)