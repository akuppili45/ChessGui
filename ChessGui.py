from tkinter import *
import itertools

window = Tk()
window.resizable(width=False, height=False)

'''
Labels and Creates the grid
'''


class Chessboard:
    xBoardLocation = 30
    yBoardLocation = 30
    canvasArray = [[Canvas for i in range(8)] for j in range(8)]
    '''
    Creates a canvas of a certain length and with.
    '''

    def __init__(self, num_squares, box_length):
        """
        Initializes a chessboard
        :param num_squares: number of squares long
        :param box_length: length of a single square
        """
        dimension = str(box_length * (num_squares + 1))
        window.geometry(dimension + "x" + dimension)
        colors = ['bisque', 'salmon4']
        colors = itertools.cycle(colors)
        for row in range(num_squares):
            for col in range(num_squares):
                block = Canvas(window, width=box_length, height=box_length)
                block.place(x=self.xBoardLocation + row * box_length, y=self.yBoardLocation + col * box_length)
                block.create_rectangle(0, 0, box_length, box_length, fill=next(colors))
                self.canvasArray[row][col] = block

            next(colors)
            self.label_board_letters(num_squares, box_length)
            self.label_board_num(num_squares, box_length)

    def label_board_num(self, num_squares, box_length):
        """
        Labels ranks
        :param num_squares: number of squares
        :param box_length: length of each square
        """
        x_pos = self.xBoardLocation - box_length / 4
        y_pos = self.yBoardLocation + box_length / 4  # constant
        for pos in range(num_squares):
            Label(text=(num_squares - pos)).place(x=x_pos, y=y_pos)
            y_pos += box_length

    def label_board_letters(self, num_squares, box_length):
        """
        Labels files
        :param num_squares: number of squares
        :param box_length: length of each square
        """
        board_constant = 5 / 4
        x_pos = self.xBoardLocation + box_length / 4
        y_pos = self.yBoardLocation + (num_squares - 1 + board_constant) * box_length  # constant
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        for pos in range(num_squares):
            Label(text=letters[pos]).place(x=x_pos, y=y_pos)
            x_pos += box_length


def main():
    main_board = Chessboard(8, 80)
    window.mainloop()


if __name__ == "__main__":
    main()
