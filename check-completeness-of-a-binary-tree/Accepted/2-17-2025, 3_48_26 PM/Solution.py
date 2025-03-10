// https://leetcode.com/problems/check-completeness-of-a-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        q=deque([root])

        isComplete=False

        while q:
            node=q.popleft()

            if node is None:
                isComplete=True
            else:
                if isComplete:
                    return False
                
                q.append(node.left)
                q.append(node.right)

        return True