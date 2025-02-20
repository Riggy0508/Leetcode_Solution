// https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        col_map=defaultdict(list)
        
        q=deque([(root,0,0)])

        while q:
            node,row,col=q.popleft()

            if node:
                col_map[col].append((row,node.val))
            
            if node.left:
                q.append((node.left,row+1,col-1))
            if node.right:
                q.append((node.right,row+1,col+1))
            

        sorted_col=sorted(col_map.keys())
        def custom_sort(t):
            return (t[0],t[1])
        result=[]
        for col in sorted_col:
            col_node=col_map[col]

            col_node.sort(key=custom_sort)

            result.append([val for i,val in col_node])

        return result

        

