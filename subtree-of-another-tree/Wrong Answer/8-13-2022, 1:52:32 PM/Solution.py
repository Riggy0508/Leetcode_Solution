// https://leetcode.com/problems/subtree-of-another-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:return True
        if not subRoot: return False
        
        
        if self.sameTree(subRoot,root):
            return True
        return (self.isSubtree(subRoot.right,root)or self.isSubtree(subRoot.left,root))
    
    def sameTree(self,subRoot,root):
        if not subRoot and not root:
            return True
        if subRoot and root and subRoot.val==root.val:
            return (self.sameTree(subRoot.left,root.left) and self.sameTree(subRoot.right,root.right))
        return False