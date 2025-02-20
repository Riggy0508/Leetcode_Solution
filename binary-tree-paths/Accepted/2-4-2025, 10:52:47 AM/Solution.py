// https://leetcode.com/problems/binary-tree-paths

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths=[]

        def dfs(node,cur_path):
            if not node:
                return 

            if cur_path:
                cur_path+="->"+str(node.val)
            else:
                cur_path=str(node.val)

            if not node.left and not node.right:
                paths.append(cur_path)
            else:
                dfs(node.left,cur_path)
                dfs(node.right,cur_path)

        dfs(root,"")
        return paths