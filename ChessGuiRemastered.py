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




    '''
    def get_hypotenuse(self):
        global button_releaseX
        global button_releaseY
        global button_releaseX2
        global button_releaseY2
        hypotenuse = self.distance(self.button_releaseX,self.button_releaseY,self.button_releaseX2,self.button_releaseY2)
        return hypotenuse
    '''
    # def button_released(self,event):
    #     global button_releaseX
    #     global button_releaseY
    #     self.button_releaseX = event.x
    #     self.button_releaseY = event.y
    #
    # def button_pressed(self, event):
    #     global button_releaseX2
    #     global button_releaseY2
    #     self.button_releaseX2 = event.x
    #     self.button_releaseY2 = event.y


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

    def __init__(self, num_of_squares_per_side, w, h):
            self.initialY = 95
            resize = Resize()
            for row in range(int(num_of_squares_per_side / 2)):
                for i in range(int(num_of_squares_per_side / 2)):
                    newCanvas = Canvas(root, width=w, height=h)
                    newCanvas.place(x=self.x, y=self.y)
                    box = newCanvas.create_rectangle(0, 0, w, h, fill='bisque')
                    anotherCanvas = Canvas(root, width=w, height=h)
                    anotherCanvas.place(x=self.x, y=self.y + h)
                    box1 = anotherCanvas.create_rectangle(0, 0, w, h, fill='salmon4')
                    newCanvas = Canvas(root, width=w, height=h)
                    newCanvas.place(x=self.x + w, y=self.y)
                    box2 = newCanvas.create_rectangle(0, 0, w, h, fill='salmon4')
                    anotherCanvas = Canvas(root, width=w, height=h)
                    anotherCanvas.place(x=self.x + w, y=self.y + h)
                    box3 = anotherCanvas.create_rectangle(0, 0, w, h, fill='bisque')
                    self.y += 2 * h
                self.x += 2 * w
                self.y = self.initialY
                self.labelLetters()
                self.labelNumbers()
            root.bind("<Button-1>", resize.get_button_click_coordinates)


class Resize:
    def distance(self, x, y, x1, y1):
        changeX = x - x1
        changeY = y - y1
        distance = math.sqrt((changeX * changeX) + (changeY * changeY))
        return distance

    def resize(self, event, canvas_width, canvas_height):
        height_change = self.distance(event.x, event.y, event.x, self.get_button_click_coordinates()[1])
        width_change = self.distance(event.x, self.get_button_click_coordinates()[1], self.get_button_click_coordinates()[0], self.get_button_click_coordinates()[1])
        total_width = 8*canvas_width
        total_height=8*canvas_height
        total_width += total_width+2*width_change
        total_height+= total_height+2*height_change
        new_canvas_width = total_width/8
        new_canvas_height = total_height/8
        changesize = [new_canvas_width, new_canvas_height]


    def get_button_click_coordinates(self, event):
        coord = [event.x, event.y]
        return coord
 


main_board = Chessboard(8,80,80)



root.mainloop()