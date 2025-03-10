// https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        hash1=defaultdict(list)

        result=[]

        q=deque([(root,0,0,)])

        while q:
            node,row,col=q.popleft()

            hash1[col].append((row,node.val))

            if node.left:
                q.append((node.left,row+1,col-1))

            if node.right:
                q.append((node.right,row+1,col+1))


        sort=sorted(hash1.keys())

        def customSort(t):
            return [t[0],t[1]]


        for index in sort:
            value=hash1[index]

            valueSort=sorted(value,key=customSort)

            result.append([val for i,val in valueSort])

        return result