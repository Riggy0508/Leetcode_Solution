// https://leetcode.com/problems/bus-routes

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source==target:
            return 0
        
        graph=defaultdict(set)
        for route_id,stops in enumerate(routes):
            for stop in stops:
                graph[stop].add(route_id)
        
        queue=deque([(source,0)])
        seen_routes=set()
        seen_stops=set([source])
        
        while queue:
            stop, num_changes = queue.popleft()
            if stop==target:
                return num_changes
            
            for route_id in graph[stop]:
                if route_id not in seen_routes:
                    seen_routes.add(route_id)
                    for stop in routes[route_id]:
                        if stop not in seen_stops:
                            seen_stops.add(stop)
                            queue.append((stop,num_changes+1))
        return -1
                    