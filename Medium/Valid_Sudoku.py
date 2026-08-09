class Solution:
    def isValidSudoku(self, board):

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):

                num = board[row][col]

                # Ignore empty cells
                if num == ".":
                    continue

                box = (row // 3) * 3 + (col // 3)

                # Check for duplicate
                if num in rows[row]:
                    return False

                if num in cols[col]:
                    return False

                if num in boxes[box]:
                    return False

                # Add number
                rows[row].add(num)
                cols[col].add(num)
                boxes[box].add(num)

        return True
