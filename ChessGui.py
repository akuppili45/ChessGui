'''
TODO:
    - fix hardcoding
    - make the board resizeable
    - make the letters and numbers resizeable to the same scale as the board
    - fix transparencies in gimp
'''
from tkinter import *
import ctypes

window = Tk()
window.resizable(width=False, height=False)

'''
Labels and Creates the grid
'''

user32 = ctypes.windll.user32
window.geometry(str(int(user32.GetSystemMetrics(0) / 2)) + "x" + str(user32.GetSystemMetrics(1)))


class Chessboard:
    screen_height = window.winfo_screenheight()

    xBoardLocation = 30
    yBoardLocation = 30
    canvasArray = [[Canvas for i in range(8)] for j in range(8)]
    '''
    Creates a canvas of a certain length and with.
    '''

    def __init__(self, num_squares, box_length):
        # resize = Resize()
        for row in range(int(num_squares)):
            for col in range(int(num_squares)):
                block = Canvas(window, width=box_length, height=box_length)
                block.place(x=self.xBoardLocation + row * box_length, y=self.yBoardLocation + col * box_length)
                if (col + row) % 2 == 0:
                    block.create_rectangle(0, 0, box_length, box_length, fill='bisque')
                else:
                    block.create_rectangle(0, 0, box_length, box_length, fill='salmon4')
                self.canvasArray[row][col] = block
            self.label_board_letters(num_squares, box_length)
            self.label_board_num(num_squares, box_length)

    def label_board_num(self, num_squares, box_length):
        x_pos = self.xBoardLocation - box_length / 4
        y_pos = self.yBoardLocation + box_length / 4  # constant
        for pos in range(num_squares):
            Label(text=(num_squares - pos)).place(x=x_pos, y=y_pos)
            y_pos += box_length

    def label_board_letters(self, num_squares, box_length):
        board_constant = 5 / 4
        x_pos = self.xBoardLocation + box_length / 4
        y_pos = self.yBoardLocation + (num_squares - 1 + board_constant) * box_length  # constant
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        for pos in range(num_squares):
            Label(text=letters[pos]).place(x=x_pos, y=y_pos)
            x_pos += box_length

main_board = Chessboard(8, 80)

window.mainloop()
