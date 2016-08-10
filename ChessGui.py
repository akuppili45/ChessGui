from tkinter import *

root = Tk()
initialY = 95
w = 80
h = 80
header = Label(text="Chess_py", anchor=CENTER, font="TimesNewRoman")
header.pack()


def create_alternating_color_grid(num_of_squares_per_side):
    x = 450
    y = 95
    for row in range(int(num_of_squares_per_side / 2)):
        for i in range(int(num_of_squares_per_side / 2)):
            newcanvas = Canvas(root, width=w, height=h)
            newcanvas.place(x=x, y=y)
            newcanvas.create_rectangle(0, 0, w, h, fill='bisque')
            anothercanvas = Canvas(root, width=w, height=h)
            anothercanvas.place(x=x, y=y + h)
            anothercanvas.create_rectangle(0, 0, w, h, fill='salmon4')
            newcanvas = Canvas(root, width=w, height=h)
            newcanvas.place(x=x + w, y=y)
            newcanvas.create_rectangle(0, 0, w, h, fill='salmon4')
            anothercanvas = Canvas(root, width=w, height=h)
            anothercanvas.place(x=x + w, y=y + h)
            anothercanvas.create_rectangle(0, 0, w, h, fill='bisque')
            y += 2 * h
        x += 2 * w
        y = initialY


def labelNumbers():
    labelX = 400
    # middle of the canvas
    initialLabelY = 135
    xy = 8
    for num in range(8):
        numLabel = Label(text=str(xy))
        numLabel.place(x=labelX, y=initialLabelY)
        initialLabelY += 80
        xy -= 1


def labelLetters():
    letterLabelX = 490
    letterLabelY = 755  # constant
    lettersOfAlphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    for l in range(8):
        labelList = Label(text=lettersOfAlphabet[l])
        labelList.place(x=letterLabelX, y=letterLabelY)
        letterLabelX += 80


def drag_and_drop(event):
    print()
    '''
    def __init__(self, num_of_squares_per_side,size):
        self.initialY = 95
        self.x = 450
        self.y = 95

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
                box2 = newCanvas.create_rectangle(0, 0, size,size, fill='salmon4')
                anotherCanvas = Canvas(root, width=size, height=size)
                anotherCanvas.place(x=self.x + size, y=self.y + size)
                box3 = anotherCanvas.create_rectangle(0, 0, size, size, fill='bisque')
                self.y += 2 * size
            self.x += 2 * size
            self.y = self.initialY
            self.labelLetters()
            self.labelNumbers()
            newCanvas.bind("B1-Motion", self.resize_board)
'''


create_alternating_color_grid(8)
labelNumbers()
labelLetters()
root.mainloop()
