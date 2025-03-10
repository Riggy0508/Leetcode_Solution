// https://leetcode.com/problems/sum-root-to-leaf-numbers

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def helper(root,current_sum):
            if not root:
                return 0

            current_sum=current_sum*10+int(root.val)

            if not root.left and not root.right:
                return current_sum

            return helper(root.left, current_sum) + helper(root.right, current_sum)

        return helper(root,0)