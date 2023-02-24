// https://leetcode.com/problems/valid-sudoku

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #Creating a set for each row, col and the 3x3 grid
        
        rows=collections.defaultdict(set)
        cols=collections.defaultdict(set)
        square=collections.defaultdict(set)   ##store the key pair
        
        for r in range(9):
            for c in range(9):
                
                #As given in the questions we need not do anythign when it comes to empty places
                if board[r][c]==".":
                    continue
                else:
                    if board[r][c] not in rows[r] or board[r][c] not in cols[c] or board[r][c] not in square[(r//3,c//3)]:
                        rows[r].add(board[r][c])
                        cols[c].add(board[r][c])
                        square[(r//3,c//3)].add(board[r][c])
                    else:
                        return False
                    
                    
        return True
                    
                    
        