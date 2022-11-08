// https://leetcode.com/problems/flatten-binary-tree-to-linked-list

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        #Pre-order Traversal = Root, Left, Right
        
        def dfs(node):
            if not node:
                return None
        
            leftTail=self.flatten(node.left)
            rightTail=self.flatten(node.right)

            if leftTail:
                leftTail.right=node.right
                node.right=node.left
                node.left=None
                
            ans=rightTail or leftTail or node

            return ans
        
        return dfs(root)
        
        
        