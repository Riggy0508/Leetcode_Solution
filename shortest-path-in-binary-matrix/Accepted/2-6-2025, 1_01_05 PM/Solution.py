// https://leetcode.com/problems/shortest-path-in-binary-matrix

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n=len(grid)

        if grid[0][0]==1 or grid[n-1][n-1]:
            return -1

        q=deque([(0,0,1)])

        grid[0][0]=1

        directions=[[0,1],[0,-1],[-1,0],[1,0],[-1,-1],[-1,1],[1,-1],[1,1]]


        while q:
            r,c,distance=q.popleft()

            if r==n-1 and c==n-1:
                return distance

            for dr,dc in directions:
                row=dr+r
                col=dc+c

                if 0<=row<n and 0<=col<n and grid[row][col]==0:
                    q.append((row,col,distance+1))

                    grid[row][col]=1

        return -1