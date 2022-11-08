// https://leetcode.com/problems/sum-root-to-leaf-numbers

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        output=[]
        
        def helper(node,sofar):
            if not node.left and not node.right:
                #output.append(sofar+[node.val])
                output.append("".join(sofar+[str(node.val)]))
    
            if node.left:
                helper(node.left,sofar+[str(node.val)])
            if node.right:
                helper(node.right,sofar+[str(node.val)])
            
        helper(root,[])
        return sum(int(x) for x in output)