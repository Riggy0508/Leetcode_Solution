// https://leetcode.com/problems/boundary-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return 

        def isLeaf(node):
            return node and not node.left and not node.right

        def dfs(node,isLeft,isRight):
            if not node:
                return 

            if isLeft and not isLeaf(node):
                result.append(node.val)
            
            if isLeaf(node):
                result.append(node.val)

            dfs(node.left,isLeft,isRight and not node.right)
            dfs(node.right,isLeft and not node.left,isRight)

            if isRight and not isLeaf(node):
                result.append(node.val)

        result=[]
        if not isLeaf(root):
            result.append(root.val)

        dfs(root.left,isLeft=True,isRight=False)
        dfs(root.right,isLeft=False,isRight=True)

        return result
            