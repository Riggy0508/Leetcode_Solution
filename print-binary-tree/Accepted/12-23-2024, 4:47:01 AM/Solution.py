// https://leetcode.com/problems/print-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        

        def height(node):
            if node is None:
                return -1

            return 1+max(height(node.left),height(node.right))

        def dfs(node,row,col):
            if node is None:
                return

            matrix[row][col]=str(node.val)
            offset=2**(tr_height-row-1)

            dfs(node.left,row+1,col-offset)
            dfs(node.right,row+1,col+offset)

        tr_height=height(root)

        rows,cols=tr_height+1,2**(tr_height+1)-1
        matrix=[["" for _ in range(cols)] for _ in range(rows)]

        dfs(root,0,(cols-1)//2)

        return matrix