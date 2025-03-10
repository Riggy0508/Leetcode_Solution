// https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        graph=defaultdict(list)

        def build_graph(cur,parent):
            if cur and parent:
                graph[cur.val].append(parent.val)
                graph[parent.val].append(cur.val)

            if cur.left:
                build_graph(cur.left,cur)
            if cur.right:
                build_graph(cur.right,cur)

        build_graph(root,None)
        visited=set()
        ans=[]
        visited.add(target.val)
        q=deque([(target.val,0)])

        while q:
            cur,distance=q.popleft()

            if distance==k:
                ans.append(cur)

            for neigh in graph[cur]:
                if neigh not in visited:
                    visited.add(neigh)
                    q.append((neigh,distance+1))    

        return ans