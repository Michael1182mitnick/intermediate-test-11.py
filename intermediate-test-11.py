# Write a function to validate if a given 9x9 Sudoku board is valid.

def is_valid_sudoku(board):
    # Use sets to track seen numbers in rows, columns, and subgrids
    rows = [set() for _ in range(9)]
    columns = [set() for _ in range(9)]
    subgrids = [set() for _ in range(9)]

    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num == '.':
                continue

            # Calculate subgrid index
            subgrid_index = (i // 3) * 3 + (j // 3)

            # Check if number is already seen in the current row, column, or subgrid
            if num in rows[i] or num in columns[j] or num in subgrids[subgrid_index]:
                return False

            # Add the number to the respective sets
            rows[i].add(num)
            columns[j].add(num)
            subgrids[subgrid_index].add(num)

    return True


# Example usage
sudoku_board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

result = is_valid_sudoku(sudoku_board)
print(f"The Sudoku board is {'valid' if result else 'invalid'}.")
