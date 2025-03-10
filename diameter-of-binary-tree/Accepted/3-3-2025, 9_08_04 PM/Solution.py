// https://leetcode.com/problems/diameter-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 
        def dfs(node):
            if not node:
                return 0
            
            leftDia=dfs(node.left)
            rightDia=dfs(node.right)

            self.diameter=max(self.diameter,rightDia+leftDia)

            return max(leftDia,rightDia)+1
    
        self.diameter=0
        dfs(root)
        return self.diameter