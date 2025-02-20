// https://leetcode.com/problems/all-paths-from-source-lead-to-destination

class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph=defaultdict(list)

        for start,end in edges:
            graph[start].append(end)

        visited=set()


        def dfs(source):

            if source ==destination:
                return len(graph[source])==0


            if source in visited or not graph[source]:
                return False

            
            visited.add(source)

            for adj in graph[source]:
                if not dfs(adj):
                    return False
                
            visited.remove(source)
            return True

        return dfs(source)
