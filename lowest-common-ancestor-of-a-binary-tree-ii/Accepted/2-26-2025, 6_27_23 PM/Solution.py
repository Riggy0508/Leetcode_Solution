// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-ii

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def lca(root):     
            if not root:
                return None

            if root.val==p.val or root.val==q.val:
                return root

            left=lca(root.left)
            right=lca(root.right)

            if left and right:
                return root

            return left if left else right

        def doesExist(root,target):
            if not root:
                return False
            if root==target:
                return True
            return doesExist(root.left, target) or doesExist(root.right, target)
            
        if doesExist(root, p) and doesExist(root, q):
            return lca(root)
        return None

        