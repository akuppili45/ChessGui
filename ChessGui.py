from tkinter import *
root = Tk()
x = 450
initialY = 95
y = 95
w = 80
h = 80
header = Label(text = "Chess_py", anchor = CENTER, font = "TimesNewRoman")
header.pack()
for row in range(4):
    for i in range(4):
        newCanvas = Canvas(root, width=w, height=h)
        newCanvas.place(x=x, y=y)
        box = newCanvas.create_rectangle(0, 0, w, h, fill='white')
        anotherCanvas = Canvas(root, width=w, height=h)
        anotherCanvas.place(x=x, y=y + h)
        box1 = anotherCanvas.create_rectangle(0, 0, w, h, fill='black')
        newCanvas = Canvas(root, width=w, height=h)
        newCanvas.place(x=x+w, y=y)
        box2 = newCanvas.create_rectangle(0, 0, w, h, fill='black')
        anotherCanvas = Canvas(root, width=w, height=h)
        anotherCanvas.place(x=x+w, y=y + h)
        box3 = anotherCanvas.create_rectangle(0, 0, w, h, fill='white')
        y += 2*h
    x += 2*w
    y = initialY
def labelNumbers():
    labelX = 400
    # middle of the canvas
    initialLabelY = 135
    xy = 8
    for num in range(8):
        numLabel = Label(text = str(xy))
        numLabel.place(x = labelX, y = initialLabelY)
        initialLabelY += 80
        xy-=1
def labelLetters():
    letterLabelX = 490
    letterLabelY = 755#constant
    lettersOfAlphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    for l in range(8):
        labelList = Label(text = lettersOfAlphabet[l])
        labelList.place(x = letterLabelX, y = letterLabelY)
        letterLabelX += 80
labelNumbers()
labelLetters()
root.mainloop()