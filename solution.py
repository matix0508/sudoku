BOARD = [
    [0, 0, 0, 9, 0, 0, 0, 0, 3],
    [3, 4, 0, 0, 1, 0, 6, 0, 0],
    [0, 5, 6, 4, 0, 0, 0, 0, 8],
    [1, 3, 2, 6, 5, 8, 0, 0, 0],
    [0, 9, 0, 7, 4, 3, 0, 6, 0],
    [0, 6, 4, 2, 9, 1, 8, 0, 0],
    [0, 2, 0, 0, 8, 0, 3, 1, 9],
    [0, 0, 0, 0, 2, 0, 0, 8, 0],
    [0, 8, 0, 0, 0, 9, 4, 5, 0]
]



def print_board(bo):

    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("\t- - - - - - - - - - - - -")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 0:
                print("\t" + str(bo[i][j]), end=" ")
            elif j == len(bo[0]) - 1:
                print(str(bo[i][j]) + " ")
            else:
                print(str(bo[i][j]) + " ", end="")
    print("\n\n")

#print_board(BOARD)


def find_blank(bo):
    blank = []
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                if (i, j) not in blank:
                    blank.append((i, j))
    return blank


def square(x, y):
    if y < 3:
        r = 0
    elif y < 6:
        r = 1
    else:
        r = 2
    if x < 3:
        c = 0
    elif x < 6:
        c = 1
    else:
        c = 2
    return c, r


def check(bo, x, y):
    num = bo[x][y]
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if (x, y) != (i, j):
                if i == x or j == y:
                    if bo[i][j] == num:
                        # print("x or y")
                        return False

                if square(i, j) == square(x, y):
                    if bo[i][j] == num:
                        # print("square")
                        return False

    return True


def find_num(bo, x, y):
    bo[x][y] += 1
    # print(bo[x][y])
    while not check(BOARD, x, y) or bo[x][y] >= 10:
        # print_board(BOARD)
        # print(f"i - {check(BOARD, x, y)}")
        bo[x][y] += 1
        if bo[x][y] >= 10:
            break
        if check(BOARD, x, y):
            break


def type_item(board, allow=False, blank=[]):

    row = int(input("Row = "))
    column = int(input("Column = "))
    item = input(f"Row: {row + 1}, Column {column + 1}, Value = ")
    board[row][column] = item
    return board


def type_own():
    answer = "Yes"
    new_board = []
    for i in range(9):
        new_board.append([])
    print("""
Ok let's get to typing your own sudoku.
To do that, I need you to type your numbers from left to right row by row
If you make a mistake at the end I will ask you if you want to make some changes.
When there is a blank space in your sudoku Type "0"
    """)
    running = True
    row = 0
    column = 0
    while running:
        item = input(f"Row: {row + 1}, Column {column + 1}, Value = ")
        new_board[row][column] = item
        if column != 8:
            column += 1
        elif row != 8:
            row += 1
        else:
            while answer == "Yes":
                print_board(new_board)
                answer = input("Here is your board. Do you want to make any changes? (Yes/No)")
                if answer == "Yes":
                    new_board = type_item(new_board)

    return new_board


def solve(board):
    blank = find_blank(board)
    checking = False
    print("Choose how do you want to play.")
    answer = input("If you make an error, Should I tell something? (Yes/No): ")
    if answer == "Yes":
        checking = True
    running = True
    while running:
        print_board(board)
        print("Choose location in which you want to type your number")




def menu():
    board = BOARD
    print("""
Hello!
What would you like to do?
1) input your own sudoku
2) solve sudoku on your own
3) see the solution (If not typed it will be default sudoku
0) Exit
    """)
    answer = int(input("Choice: "))
    if answer == 1:
        board = type_own()
    if answer == 2:



def solution(bo):

    i = 0
    while i != len(blank):

        (x, y) = blank[i]
        find_num(bo, x, y)
        if bo[x][y] >= 10:
            bo[x][y] = 0
            i -= 1
        else:
            i += 1

        if i < 0:
            print("SUDOKU has no solution")
            break
    return bo
        # print_board(bo)

blank = []
find_blank(BOARD)
print_board(BOARD)
BOARD = solution(BOARD)
print_board(BOARD)
