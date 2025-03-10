// https://leetcode.com/problems/sum-of-left-leaves

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def pro_subTree(node,is_left):
            total=0
            if node.left is None and node.right is None:
                return node.val if is_left else 0
            
            if node.left:
                total+=pro_subTree(node.left,True)
            if node.right:
                total+=pro_subTree(node.right,False)
            return total
            
        return pro_subTree(root,False)