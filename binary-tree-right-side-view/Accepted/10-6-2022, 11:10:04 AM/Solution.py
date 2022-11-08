// https://leetcode.com/problems/binary-tree-right-side-view

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Check out my Reference to solve BFS problem solved by me https://leetcode.com/problems/binary-tree-level-order-traversal/discuss/2648277/Pythonor-Validate-Binary-Search-Tree
#This is a typical BFS solution with just a minute tweak and that is, each time we try to add item's in the queue we are gonna make a note of #the right Most element and only append that in the result.
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        q=collections.deque()
        q.append(root)
        
        while q:
            qLen=len(q)
            rightSide=None
            for i in range(qLen):
                node=q.popleft()
                if node:
                    rightSide=node      #This line make's note of the most recent right Side node
                    q.append(node.left)
                    q.append(node.right)
            
            if rightSide:
                res.append(rightSide.val)
        return res