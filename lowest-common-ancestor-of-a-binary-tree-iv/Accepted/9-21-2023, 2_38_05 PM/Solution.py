// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iv

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        def dfs(root):
            if not root or root.val in s:
                return root
            left,right=dfs(root.left),dfs(root.right)
            if left and right:
                return root
            return left or right

        s={node.val for node in nodes}
        return dfs(root)