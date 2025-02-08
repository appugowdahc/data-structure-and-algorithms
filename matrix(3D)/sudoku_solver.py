class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.

        """
        def is_valid(board, row, col, num):
            # Check if 'num' is not in the current row, column, and 3x3 sub-box
            for i in range(9):
                if board[row][i] == num:
                    return False
                if board[i][col] == num:
                    return False
                if board[(row // 3) * 3 + i // 3][(col // 3) * 3 + i % 3] == num:
                    return False
            return True

        def solve(board):
            for row in range(9):
                for col in range(9):
                    if board[row][col] == '.':
                        for num in '123456789':
                            if is_valid(board, row, col, num):
                                board[row][col] = num
                                if solve(board):
                                    return True
                                board[row][col] = '.'  # Backtrack
                        return False
            return True

        solve(board)
        return board
        