// https://leetcode.com/problems/diameter-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def dfs(curr):
            if not curr:
                return 0

            left_dia=dfs(curr.left)
            right_dia=dfs(curr.right)

            self.diameter=max(self.diameter,left_dia+right_dia)

            return max(left_dia,right_dia)+1

        self.diameter=0
        dfs(root)
        return self.diameter