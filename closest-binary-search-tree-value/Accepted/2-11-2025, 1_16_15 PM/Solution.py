// https://leetcode.com/problems/closest-binary-search-tree-value

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest=root.val

        while root:
            if abs(closest-target)>abs(root.val-target) or (abs(root.val-target)==abs(closest-target) and root.val<closest):
                closest=root.val
            
            root=root.left if target<root.val else root.right

        return closest

