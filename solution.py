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
blank = []
back = False

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
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                if (i, j) not in blank:
                    blank.append((i, j))


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
    return (c, r)


def check(bo, x, y):
    num = bo[x][y]
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if (x, y) != (i, j):
                if (i == x or j == y):
                    if bo[i][j] == num:
                        #print("x or y")
                        return False

                if square(i, j) == square(x, y):
                    if bo[i][j] == num:
                        #print("square")
                        return False

    return True

def find_num(bo, x, y):
    bo[x][y] += 1
    #print(bo[x][y])
    while not check(BOARD, x, y) or bo[x][y] >= 10:
        #print_board(BOARD)
        #print(f"i - {check(BOARD, x, y)}")
        bo[x][y] += 1
        if bo[x][y] >= 10:
            break
        if check(BOARD, x, y):
            break

def solution(bo):

    i=0
    while i != len(blank):

        (x, y) = blank[i]
        find_num(bo, x, y)
        if bo[x][y] >= 10:
            bo[x][y] = 0
            i -= 1
            back = False
        else:
            i += 1

        if i < 0:
            print("SUDOKU has no solution")
            break
    return bo
        #print_board(bo)
    return bo
find_blank(BOARD)
print_board(BOARD)
BOARD = solution(BOARD)
print_board(BOARD)
