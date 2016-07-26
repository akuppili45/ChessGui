'''
TODO:
    - fix hardcoding
    - make the board resizeable
    - make the letters and numbers resizeable to the same scale as the board
    - fix transparencies in gimp
'''
from tkinter import *
import math
root = Tk()
class Chessboard:
    x = 450
    y = 95
    widgetX = 100
    widgetY = 30
    button_rel = False
    button_releaseX = 0
    button_releaseY = 0
    button_releaseX2 = 0
    button_releaseY2 = 0
    def height_change(self):
        return self.distance(self.button_releaseX2, self.button_releaseX2, self.button_releaseY2, self.button_releaseY)
    def width_change(self):
        return self.distance(self.button_releaseX2, self.button_releaseX, self.button_releaseY, self.button_releaseY)
    def distance(self, x,y,x1,y1):
        changeX = x - x1
        changeY = y - y1
        distance = math.sqrt((changeX * changeX) + (changeY * changeY))
        return distance
    def get_hypotenuse(self):
        global button_releaseX
        global button_releaseY
        global button_releaseX2
        global button_releaseY2
        hypotenuse = self.distance(self.button_releaseX,self.button_releaseY,self.button_releaseX2,self.button_releaseY2)
        return hypotenuse
    def button_released(self,event):
        global button_releaseX
        global button_releaseY
        self.button_releaseX = event.x
        self.button_releaseY = event.y
        button_rel = True
        self.get_hypotenuse()
        print(self.get_hypotenuse())

    def get_coordinates(self, event):
        global button_releaseX2
        global button_releaseY2
        self.button_releaseX2 = event.x
        self.button_releaseY2 = event.y


    def labelNumbers(self):
        self.labelX = 400
        # middle of the canvas
        self.initialLabelY = 135
        self.xy = 8
        for num in range(8):
            numLabel = Label(text=str(self.xy))
            numLabel.place(x=self.labelX, y=self.initialLabelY)
            self.initialLabelY += 80
            self.xy -= 1

    def labelLetters(self):
        self.letterLabelX = 490
        self.letterLabelY = 755  # constant
        self.lettersOfAlphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        for l in range(8):
            labelList = Label(text=self.lettersOfAlphabet[l])
            labelList.place(x=self.letterLabelX, y=self.letterLabelY)
            self.letterLabelX += 80
    def resize_board(self, event):
        if(event.x == self.x and event.y ==self.y):
            print()


    def __init__(self, num_of_squares_per_side, size):
            self.initialY = 95
            for row in range(int(num_of_squares_per_side / 2)):
                for i in range(int(num_of_squares_per_side / 2)):
                    newCanvas = Canvas(root, width=size, height=size)
                    newCanvas.place(x=self.x, y=self.y)
                    box = newCanvas.create_rectangle(0, 0, size, size, fill='bisque')
                    anotherCanvas = Canvas(root, width=size, height=size)
                    anotherCanvas.place(x=self.x, y=self.y + size)
                    box1 = anotherCanvas.create_rectangle(0, 0, size, size, fill='salmon4')
                    newCanvas = Canvas(root, width=size, height=size)
                    newCanvas.place(x=self.x + size, y=self.y)
                    box2 = newCanvas.create_rectangle(0, 0, size, size, fill='salmon4')
                    anotherCanvas = Canvas(root, width=size, height=size)
                    anotherCanvas.place(x=self.x + size, y=self.y + size)
                    box3 = anotherCanvas.create_rectangle(0, 0, size, size, fill='bisque')
                    self.y += 2 * size
                self.x += 2 * size
                self.y = self.initialY
                self.labelLetters()
                self.labelNumbers()
main_board = Chessboard(8,80)
root.bind("<Button-1>", main_board.get_coordinates)
root.bind("<ButtonRelease-1>", main_board.button_released)


root.mainloop()