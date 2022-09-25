// https://leetcode.com/problems/pacific-atlantic-water-flow

class Solution:

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        v_pac = set()
        v_atl = set()
        
        def dfs(v_set, row, col, curr_height):
            if row < 0 or row >= m or \
                col < 0 or col >= n or \
                    (row,col) in v_set or \
                        curr_height > heights[row][col]:
                return
            v_set.add((row, col))

            curr_height = heights[row][col]
            dfs(v_set, row + 1, col, curr_height)
            dfs(v_set, row - 1, col, curr_height)
            dfs(v_set, row, col + 1, curr_height)
            dfs(v_set, row, col - 1, curr_height)

        for col in range(n):
            dfs(v_pac, 0, col, heights[0][col]) # First row
            dfs(v_atl, m - 1, col, heights[m-1][col]) # Last row

        for row in range(m):
            dfs(v_pac, row, 0, heights[row][0]) # First column
            dfs(v_atl, row, n-1, heights[row][n-1]) # Last column


        result = v_atl.intersection(v_pac)

        return result