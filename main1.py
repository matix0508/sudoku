from tkinter import Tk, Label, Canvas, Frame, Button, BOTH, TOP, BOTTOM
from tkinter.filedialog import askopenfilename, asksaveasfilename

MARGIN = 20
SIDE = 50
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9

LARGE_FONT = ("Verdana", 12)


def create_board(board_file):
    board = []

    for line in board_file:
        line = line.strip()

        if len(line) != 9:
            raise SudokuError(
                "Each line in the sudoku puzzle must be 9 chars long"
            )
        board.append([])

        for c in line:
            if not c.isdigit():
                raise SudokuError(
                    "Valid characters for a sudoku puzzle must be in 0-9"
                )
            board[-1].append(int(c))
    if len(board) != 9:
        raise SudokuError(
            "Each sudoku puzzle must be 9 lines long"
        )

    return board


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


class SudokuError(Exception):
    pass


class SudokuApp(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        Tk.wm_title(self, "Sudoku Game")

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.geometry("%dx%d" % (WIDTH, HEIGHT + 40))

        self.frames = {}

        for F in (StartPage, 0):
            frame = F(container, self)

            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class SudokuBoard:
    """
    class for sudoku Board
    """

    def __init__(self, board_file):
        self.board = create_board(board_file)
        self.original_board = create_board(board_file)
        self.empty = []
        self.remaining_empty = []
        self.solved

    def find_blank(self):
        for row in range(9):
            for column in range(9):
                if self.board[row][column] == 0:
                    self.empty.append((row, column))

    def solve(self):


        i = 0
        while i != len(self.remaining_empty):

            (x, y) = self.remaining_empty[i]
            self.find_num(x, y)
            if self.board[x][y] >= 10:
                self.board[x][y] = 0
                i -= 1
            else:
                i += 1

            if i < 0:
                raise SudokuError("Sudoku has no solution!")
                # break

    def find_num(self, x, y):
        self.board[x][y] += 1
        # print(bo[x][y])
        while not self.check(x, y) or self.board[x][y] >= 10:
            # print_board(BOARD)
            # print(f"i - {check(BOARD, x, y)}")
            self.board[x][y] += 1
            if self.board[x][y] >= 10:
                break
            if self.check(x, y):
                break

    def check(self, x, y):
        num = self.board[x][y]
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if (x, y) != (i, j):
                    if i == x or j == y:
                        if self.board[i][j] == num:
                            # print("x or y")
                            return False

                    if square(i, j) == square(x, y):
                        if self.board[i][j] == num:
                            # print("square")
                            return False
        return True


class StartPage(Frame):
    """
    starting Page, user will choose what to do from here:
    options: Load file, New file, Solve
    """

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.board_file = None
        self.board = None

        label1 = Label(self, text="Welcome in the SudokuApp!", font=LARGE_FONT)
        label1.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        button1 = Button(self, text="Load file", command=self.load_file)
        button1.grid(
            row=1,
            column=0,
            sticky="nsew"
        )

    def load_file(self):
        """
        Loads the file from the computer, looks for *.sudoku
        """
        filepath = askopenfilename(
            filetypes=[("Sudoku Files", "*.sudoku")]
        )
        if not filepath:
            return
        self.board_file = filepath
