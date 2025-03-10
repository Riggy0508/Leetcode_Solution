// https://leetcode.com/problems/diameter-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:


        def dfs(cur):
            nonlocal diameter
            if not cur:
                return 0

            left=dfs(cur.left)
            right=dfs(cur.right)

            diameter=max(diameter,left+right)

            return max(left,right)+1
        
        diameter=0
        dfs(root)
        return diameter