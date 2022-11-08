// https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        
        q=collections.deque()
        q.append(root)
        
        while q:
            qLen=len(q)
            level=[]
            for _ in range(qLen):
                node=q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            
            if len(res)%2!=0 and level:
                res.append(level[::-1])
            elif len(res)%2==0 and level:
                res.append(level)
        return res
                