// https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def build_graph(self,node,parent,graph):
        if not node:
            return

        if parent:
            graph[node.val].append(parent.val)
            graph[parent.val].append(node.val)

        self.build_graph(node.left, node, graph)
        self.build_graph(node.right, node, graph)

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph=defaultdict(list)
        self.build_graph(root,None,graph)

        q=deque([target.val])
        visited=set()
        visited.add(target.val)
        distance=0

        while q:
            if distance==k:
                return list(q)
            for _ in range(len(q)):
                node=q.popleft()
                for neigh in graph[node]:
                    if neigh not in visited:
                        visited.add(neigh)
                        q.append(neigh)

            distance+=1

        return []

