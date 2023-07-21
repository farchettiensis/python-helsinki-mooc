# Write your solution here
def row_correct(sudoku: list, row_no: int):
    numbers = []
    for number in sudoku[row_no]:
        if number != 0 and number in numbers:
            return False
        numbers.append(number)
    print(numbers)
    return True

def column_correct(sudoku: list, column_no: int):
    numbers = []
    for row in sudoku:
        number = row[column_no]
        if number != 0 and number in numbers:
            return False
        numbers.append(number)
    print(numbers)
    return True

def block_correct(sudoku: list, row_no: int, column_no: int):
    numbers = []
    for i in range(row_no, row_no + 3):
        for j in range(column_no, column_no + 3):
            number = sudoku[i][j]
            if number > 0 and number in numbers:
                return False
            numbers.append(number)
    return True

def sudoku_grid_correct(sudoku: list):
    for i in range(len(sudoku)):
        if not row_correct(sudoku, i) or not column_correct(sudoku, i):
            return False
    blocks_start_points = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]
    for row, col in blocks_start_points:
        if not block_correct(sudoku, row, col):
            return False

    return True

if __name__ == "__main__":
    sudoku = [
        [9, 6, 2, 0, 8, 0, 3, 7, 0],
        [2, 0, 0, 1, 0, 0, 0, 4, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 2],
        [4, 0, 0, 0, 0, 0, 0, 0, 3],
    ]
    print(row_correct(sudoku, 0))
    print(column_correct(sudoku, 0))
    print(block_correct(sudoku, 0, 0))
    print(sudoku_grid_correct(sudoku))
