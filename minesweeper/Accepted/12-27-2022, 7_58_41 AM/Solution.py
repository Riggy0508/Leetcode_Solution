// https://leetcode.com/problems/minesweeper

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        i,j,rows,cols=click[0],click[1],len(board),len(board[0])
        def dfs(i,j):
                if board[i][j]=="E":
                    neigh=[(x,y) for x,y in ((i-1,j),(i+1,j),(i,j-1),(i,j+1),(i+1,j+1),(i-1,j-1),(i+1,j-1),(i-1,j+1)) if 0<=x<rows and 0<=y<cols]
                    cnt=sum(board[x][y]=="M" for x,y in neigh)
                    if not cnt:
                        board[i][j]="B"
                        for x,y in neigh:
                            dfs(x,y)
                    else:
                        board[i][j]=str(cnt)

        if board[i][j]=="M":
            board[i][j]="X"
        else:
            dfs(i,j)
        return board
        