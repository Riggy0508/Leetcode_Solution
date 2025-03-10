// https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#In order to solve this question, you first need to understand how to construct a preorder tree and inorder tree independently. 
#1. You need to understand that while creating a binary tree from pre and in order traversal. The first Node of preorder traversal is always gonna be the root. 
#2. You need to find the index position of the first node of pre-order in the in-order traversal list and anything towards the left of that value in the inorder traversal is gonna be left subtree of the main tree that we wanna build and anything right of that value in the list is gonna be in the right of subtree that we wanna build. 
#Apply this logic recursively and you are done.

#Try solving this no a piece of peper 2/3 times and you will understand it. 

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        
        root=TreeNode(preorder[0])
        mid=inorder.index(preorder[0])
        
        root.left=self.buildTree(preorder[1:mid+1],inorder[:mid])
        root.right=self.buildTree(preorder[mid+1:],inorder[mid+1:])
        
        return root