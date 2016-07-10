from tkinter import *
root = Tk()
x = 300
y = 95
w = 80
h = 80
'''
newCanvas = Canvas(root, width=w, height=h)
#newCanvas.pack()
newCanvas.place(x = x, y = y)
box = newCanvas.create_rectangle(0, 0, w, h, fill = 'black')
anotherCanvas = Canvas(root, width = w, height = h)
#anotherCanvas.pack()
anotherCanvas.place(x =x, y = 175)
box1 = anotherCanvas.create_rectangle(0, 0, w, h, fill='white')
'''
'''
for i in range(4):
    newCanvas = Canvas(root, width=w, height=h)
    newCanvas.place(x=x, y=y)
    box = newCanvas.create_rectangle(0, 0, w, h, fill='white')
    anotherCanvas = Canvas(root, width=w, height=h)
    anotherCanvas.place(x=x, y=y+80)
    box1 = anotherCanvas.create_rectangle(0, 0, w, h, fill='black')
    y+=160
'''
'''
a = Canvas(root, width = w, height = h)
a.place(x = x+80, y = 95)
b = a.create_rectangle(0,0,w,h,fill="orange")
'''
'''
for next in range(4):
    newCanvas = Canvas(root, width=w, height=h)
    newCanvas.place(x=x+80, y=y)
    box = newCanvas.create_rectangle(0, 0, w, h, fill='white')
    anotherCanvas = Canvas(root, width=w, height=h)
    anotherCanvas.place(x=x+80, y=y+80)
    box1 = anotherCanvas.create_rectangle(0, 0, w, h, fill='black')
    y+=160
'''
for grid in range(8):
    for i in range(4):
        newCanvas = Canvas(root, width=w, height=h)
        newCanvas.place(x=x, y=y)
        box = newCanvas.create_rectangle(0, 0, w, h, fill='white')
        anotherCanvas = Canvas(root, width=w, height=h)
        anotherCanvas.place(x=x, y=y + 80)
        box1 = anotherCanvas.create_rectangle(0, 0, w, h, fill='black')
        y += 160
    x+=80
    y=95

root.mainloop()