class Solution:
    def solveSudoku(self, board):

        def is_valid(row, col, num):

            # Check row
            for j in range(9):
                if board[row][j] == num:
                    return False

            # Check column
            for i in range(9):
                if board[i][col] == num:
                    return False

            # Check 3x3 box
            start_row = (row // 3) * 3
            start_col = (col // 3) * 3

            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if board[i][j] == num:
                        return False

            return True

        def solve():

            # Find an empty cell
            for row in range(9):
                for col in range(9):

                    if board[row][col] == ".":

                        # Try numbers 1 to 9
                        for num in "123456789":

                            if is_valid(row, col, num):

                                # Choose
                                board[row][col] = num

                                # Explore
                                if solve():
                                    return True

                                # Undo
                                board[row][col] = "."

                        # No number worked
                        return False

            # No empty cells remain
            return True

        solve()
