// https://leetcode.com/problems/valid-sudoku

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols=collections.defaultdict(set)
        rows=collections.defaultdict(set)
        square=collections.defaultdict(set)  # incldues a key value pari
        
        
        for r in range(9):
            for c in range(9):
                if board[r][c]==".":
                    continue
                
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in square[(r//3,c//3)]:
                    return False
                else:
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    square[(r//3,c//3)].add(board[r][c])
        return True
                    