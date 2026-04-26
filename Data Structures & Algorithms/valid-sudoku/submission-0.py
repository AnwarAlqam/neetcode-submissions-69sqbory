class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])

        # check columns
        for col in range(0, cols, 1):
            seen = []
            for row in range(0, rows, 1):
                if board[row][col] == ".":
                    continue
                if board[row][col] not in seen:
                    seen.append(board[row][col])
                else:
                    return False

        # check rows
        for row in range(0, rows, 1):
            seen = []
            for col in range(0, cols, 1):
                if board[row][col] == ".":
                    continue
                if board[row][col] not in seen:
                    seen.append(board[row][col])
                else:
                    return False
        
        # check cells
        for br in range(3):
            for bc in range(3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        r = br * 3 + i
                        c = bc * 3 + j
                        v = board[r][c]
                        if v == ".":
                            continue
                        if v in seen:
                            return False
                        seen.add(v)

        return True





