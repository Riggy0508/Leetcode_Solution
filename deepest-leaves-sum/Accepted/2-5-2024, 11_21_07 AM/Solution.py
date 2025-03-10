// https://leetcode.com/problems/deepest-leaves-sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q=deque()
        q.append((root,0))
        max_dept,output=0,0

        while q:
            cand,dept=q.popleft()
            if dept>max_dept:
                output=0
                max_dept=dept
            if dept==max_dept:
                output+=cand.val
            if cand.left: q.append((cand.left,dept+1))
            if cand.right: q.append((cand.right,dept+1))

        return output
