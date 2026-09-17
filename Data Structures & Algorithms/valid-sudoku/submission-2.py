class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        uq = set()

        for i in range(9):
            uq.clear()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in uq:
                    return False
                else:
                    uq.add(board[i][j])
        
        for i in range(9):
            uq.clear()
            for j in range(9):
                if board[j][i] == ".":
                    continue
                elif board[j][i] in uq:
                    return False
                else:
                    uq.add(board[j][i])
        
        for s in range(9):
            uq.clear()
            for i in range(3):
                for j in range(3):
                    row = (s//3) * 3 + i
                    col = (s%3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    elif board[row][col] in uq:
                        return False
                    else:
                        uq.add(board[row][col])
        
        return True
        
        
                




        