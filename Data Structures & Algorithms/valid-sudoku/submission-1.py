class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols=collections.defaultdict(set) # this is a hashset used to check duplicate in each row
        rows=collections.defaultdict(set) # this is a hashset used to check duplicated in each column
        squares=collections.defaultdict(set) # this is a hashset used to check the duplicates in each 3x3 square grid. This is checked by r//3 ,c//3 this gives the overall range in which it occurs
        for r in range(9):
            for c in range(9):
                if board[r][c]==".":
                    continue
                if (board[r][c] in rows [r] or board[r][c] in cols [c] or board[r][ c] in squares[(r//3,c//3)]): # here check if the elemnt in rows and columns in set if it is in it return False else add them to the set.
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])
        return True
        