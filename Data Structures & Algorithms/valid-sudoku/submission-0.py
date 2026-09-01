class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #We want to use a hashset and check each of the 3 rules for a valid sudoku board
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        n = 9
        for r in range(n):
            for c in range(n):
                #Check if empty space
                if board[r][c] == ".":
                    continue
                #Check if current position is in any of our hashsets
                if ( board[r][c] in rows[r] or
                    board[r][c] in cols[c] or 
                    board[r][c] in squares[(r//3, c//3)] ):
                    return False
                #Add current position to hashsets
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True