// https://leetcode.com/problems/kth-smallest-element-in-a-bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(root):
            if not root:
                return []
            root_left=inorder(root.left)
            root_val=[root.val]
            root_right=inorder(root.right)

            return root_left+root_val+root_right
        return inorder(root)[k-1]
        