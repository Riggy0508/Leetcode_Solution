// https://leetcode.com/problems/symmetric-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.isMirror(root.left,root.right)
    
    def isMirror(self,leftroot,rightroot):
        if leftroot and rightroot:
            return leftroot.val==rightroot.val and (self.isMirror(leftroot.left,rightroot.right) and self.isMirror(leftroot.right,rightroot.left))
        return leftroot==rightroot
        
        
        
        
        
        
        
#         if not root:
#             return True
        
#         return self.isMirror(root.left,root.right)
    
#     def isMirror(self,left,right):
#         if left and right:
#             return left.val==right.val and self.isMirror(left.left,right.right) and self.isMirror(left.right,right.left)
#         return left==right