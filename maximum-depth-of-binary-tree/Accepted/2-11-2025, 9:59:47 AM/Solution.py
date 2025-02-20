// https://leetcode.com/problems/maximum-depth-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0

        q=deque([root])
        length=0

        while q:
            for _ in range(len(q)):
                node=q.popleft()

                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)

            length+=1

        return length
            