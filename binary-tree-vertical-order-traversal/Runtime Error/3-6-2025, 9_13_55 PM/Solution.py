// https://leetcode.com/problems/binary-tree-vertical-order-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        hash1=defaultdict(list)

        q=deque([(root,0)])

        while q:
            node,col=q.popleft()

            hash1[col].append(node.val)

            if node.left:
                q.append((node.left,col-1))

            if node.right:
                q.append((node.right,col+1))

        return [hash1[key] for key in sorted(hash1.keys())]