// https://leetcode.com/problems/binary-tree-inorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #In this problem we need to return the output in the form of list, hence we will create a list in the start
        res=[]
        
        #Because we are trying to solve this using recursion, we need to define a recursive function
        def inOrder(root):
            #Handling a case where if root is present we will find the next root by traversing left and right
            if root:
                inOrder(root.left)
                #In Inorder Traversal, we start visit the left node then the root node and then the right node
                #We have traverse the left part now it's time to add teh root to our list
                res.append(root.val)
                #Looking towards the right part
                inOrder(root.right)
            
        #Base condition to call the recursion function 
        inOrder(root)
        return res