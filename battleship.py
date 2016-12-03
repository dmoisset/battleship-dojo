board = [
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
]

letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
}

for n in range(5):
    print("Where do you want ship ", n + 1, "?")
    column = input("column (A to E):")
    row = input("row (1 to 5):")
    column_number = letters_to_numbers[column]
    row_number = int(row) - 1

    board[row_number][column_number] = 'X'

    for row in board:
        print(row)
