// https://leetcode.com/problems/number-of-islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols=len(grid),len(grid[0])
        islands=0
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        visited=set()


        def bfs(r,c):
            q=collections.deque()
            q.append((r,c))
            visited.add((r,c))

            while q:
                r,c=q.popleft()
                for dr,dc in directions:
                    r1=dr+r
                    c1=dc+c

                    if r1 in range(rows) and c1 in range(cols) and grid[r][c]=="1" and (r1,c1) not in visited:
                        q.append((r1,c1))
                        visited.add((r1,c1))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visited:
                    islands+=1
                    bfs(r,c)

        return islands