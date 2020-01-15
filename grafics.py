import arcade
from solution import *
#from arcade.gui import *

STARTED = False
I = False

ROW_COUNT = 9
COLUMN_COUNT = 9

WIDTH = 50
HEIGHT = 50

MARGIN = 3

SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN
SCREEN_TITLE = 'Sudoku'

#class SolveButton(TextButton):
#    def __init__(self, game, x=0, y=0,
#                width=100, height=40,
#                text="Solve")
#        super().__init__(x, y, width, height,
#                        text, theme=None)
#        self.game = game
#
#    def on_press(self):
#        self.pressed = True
#
#    def on_release(self):
#        if self.pressed:
#            self.pressed = False

class Tile:
    def __init__(self, row=0, column=0):
        self.row = row
        self.column = column
        self.x = (MARGIN + WIDTH) * self.column + MARGIN + WIDTH // 2
        self.y = SCREEN_HEIGHT - ((MARGIN + HEIGHT) * self.row + MARGIN + HEIGHT // 2)
        self.text_size = 30
        self.text_x = self.x - 10
        self.text_y = self.y - 15

        self.text = str(BOARD[row][column])



class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.grid = []
        self.counter = 0
        for row in range(ROW_COUNT):
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(None)
                self.grid[row][column] = Tile(row, column)
        arcade.set_background_color(arcade.color.BLACK)


    def on_draw(self):

        arcade.start_render()


        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                x = self.grid[row][column].x
                y = self.grid[row][column].y
                text = self.grid[row][column].text
                text_x = self.grid[row][column].text_x
                text_y = self.grid[row][column].text_y
                text_size = self.grid[row][column].text_size
                arcade.draw_rectangle_filled(x, y,
                                            WIDTH, HEIGHT,
                                            arcade.color.WHITE)

                arcade.draw_text(text, text_x, text_y,
                                arcade.color.BLACK,
                                text_size)
    def solve(self):
        if self.counter != len(blank):
            (x, y) = blank[self.counter]
            find_num(BOARD, x, y)
            if BOARD[x][y] >= 10:
                BOARD[x][y] = 0
                self.counter -= 1
                back = False
            else:
                self.counter += 1

            if self.counter < 0:
                print("SUDOKU has no solution")
        self.grid[x][y].text = str(BOARD[x][y])

    def on_update(self, delta_time):
        self.solve()

def main():
    MyGame()
    arcade.run()

if __name__ == "__main__":
    main()
