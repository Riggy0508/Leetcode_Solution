// https://leetcode.com/problems/diameter-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            nonlocal diameter

            if not root:
                return 0

            leftDia=self.dfs(root.left)
            rightDia=self.dfs(root.right)

            diamter=max(diameter,leftDia+rightDia)

            return max(leftDia,rightDia)+1

            return diameter

        diameter=0
        dfs(root)
        return diameter