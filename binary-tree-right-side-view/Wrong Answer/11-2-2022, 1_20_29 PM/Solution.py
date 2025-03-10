// https://leetcode.com/problems/binary-tree-right-side-view

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q=collections.deque()
        
        q.append(root)
        
        res=[]
        while q:
            qLen=len(q)
            rightNode=None
            
            for i in range(qLen):
                node=q.popleft()
                if node:
                    rightNode=node.val
                    q.append(node.left)
                    q.append(node.right)
                    
            if rightNode:
                res.append(rightNode)
        return res