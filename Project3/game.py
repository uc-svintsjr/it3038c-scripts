# Name: Joseph Svintsitsky
# Module: Project 3
# Assignment:  Project 3 will bring the breadth of knowledge that you have acquired in this class and allow you to create almost anything you want. 
# Using any of the skills we’ve used thus far, or any of the skills you are working with in other classes, build a project that either builds on the previous projects, or is it's own thing.
# Due Date: 11/30/2021
# Resources: https://docs.python.org/3/library/tkinter.html
# Resources: https://www.youtube.com/watch?v=yQSEXcf6s2I
import numpy as np
from tkinter import *
import keyboard

# This function is for giving random dimensions of height and width to all the walls
def randdim():              
    x = int(np.random.randint(5, 10, 1))
    y = int(np.random.randint(25, 50, 1))
    return x, y

# These variables (wall) are how seperated each wall can be and randdim is the height and width of the walls
# wall 1 [x coordinate,(dimensions from randim)]
wall1 = [0, randdim()]
# wall 2 [x coordinate,(dimensions from randim)]
wall2 = [200, randdim()]       
# wall 3 [x coordinate,(dimensions from randim)]
wall3 = [400, randdim()]
# wall 4 [x coordinate,(dimensions from randim)]       
wall4 = [600, randdim()]
# wall 5 [x coordinate,(dimensions from randim)]      
wall5 = [800, randdim()]

# ball   [y coordinate,(dimensions from randim)]
# 200 is the floor x value, 30,30 is the dimensions of the ball      
ball = [200, (30, 30)]  
# boolean for upward jump      
upward = 0  
# boolean for downward jump                     
downward = 0                       
# boolean for jump
jump = 0          
# points          
point = 0
# Game over              
end = 0                    

# This function is used for resetting values for new game
def reset():                
    global wall1
    global wall2
    global wall3
    global wall4
    global wall5
    global ball
    global upward
    global downward
    global jump
    global point

    #jump = 0
    #upward = 0
    #downward = 0
    #point = 0
    #end = 0

    #wall1 = [0, randdim()]
    #wall2 = [200, randdim()]
    #wall3 = [400, randdim()]
    #wall4 = [600, randdim()]
    #wall5 = [800, randdim()]
    #ball = [200, (20, 20)]

def rect(l, canvas):        # for creating rectangular walls
    n = l[0]
    dim = l[1]
    y = 200
    canvas.create_rectangle(n, y, n + dim[0], y - dim[1], fill="#476042")

def circle(ball, canvas):      #for creation of Ball
    n = 50
    dim = ball[1]
    y = ball[0]
    canvas.create_oval(n, y - dim[1], n + dim[0], y, fill="yellow")

def destroy():
    w.destroy()
    display()

def endfunct(w):            # for end Display
    w.create_text(350, 100, text='Game Over')

def touch(ball):               #if ball touch the wall
    global wall1
    global wall2
    global wall3
    global wall4
    global wall5
    global end

    if wall1[0] < 75 and wall1[0] > 25:
        for i in range(wall1[1][1]):
            check = np.add(np.square(60 - wall1[0]), np.square(ball[0] - 210 + i))
            if check == np.square(10):
                end = 1
                break
    if wall2[0] < 75 and wall2[0] > 25:
        for i in range(wall2[1][1]):
            check = np.add(np.square(60 - wall2[0]), np.square(ball[0] - 210 + i))
            if check == np.square(10):
                end = 1
                break

    if wall3[0] < 75 and wall3[0] > 25:
        for i in range(wall3[1][1]):
            check = np.add(np.square(60 - wall3[0]), np.square(ball[0] - 210 + i))
            if check == np.square(10):
                end = 1
                break

    if wall4[0] < 75 and wall4[0] > 25:
        for i in range(wall4[1][1]):
            check = np.add(np.square(60 - wall4[0]), np.square(ball[0] - 210 + i))
            if check <= np.square(10):
                end = 1
                break

    if wall5[0] < 75 and wall5[0] > 25:
        for i in range(wall5[1][1]):
            check = np.add(np.square(60 - wall5[0]), np.square(ball[0] - 210 + i))
            if check == np.square(10):
                end = 1
                break

def logic():                # for placement of object
    global wall1
    global wall2
    global wall3
    global wall4
    global wall5
    global ball
    global upward
    global downward
    global jump
    global point

    if wall1[0] <= 0:
        n = np.random.randint(50, 100)
        wall1 = [950 + n, randdim()]
    else:
        wall1[0] -= 1

    if wall2[0] <= 0:
        n = np.random.randint(30, 70)
        wall2 = [950 + n, randdim()]
    else:
        wall2[0] -= 1

    if wall3[0] <= 0:
        n = np.random.randint(30, 70)
        wall3 = [950 + n, randdim()]
    else:
        wall3[0] -= 1

    if wall4[0] <= 0:
        n = np.random.randint(30, 70)
        wall4 = [950 + n, randdim()]
    else:
        wall4[0] -= 1

    if wall5[0] <= 0:
        n = np.random.randint(30, 70)
        wall5 = [950 + n, randdim()]
    else:
        wall5[0] -= 1

    if keyboard.is_pressed(' '):            # for getting value from keyboard
        jump = 1
        if ball[0] == 200:
            upward = 0
            downward = 0

    if jump == 1:           # for one complet jump

        if upward < 80:          #upward movement
            ball[0] = ball[0] - 1
            upward += 1

        if upward == 80 and downward < 80:      # downward movement
            ball[0] = ball[0] + 1
            downward += 1

        if upward == 80 and downward == 80:     #check weather ball touch the ground
            jump = False

    if wall1[0] == 50 or wall2[0] == 50 or wall3[0] == 50 or wall4[0] == 50 or wall5[0] == 50:     # calculate points
        point += 1

    touch(ball)

def display():              # for display of game window
    global w
    global wall1
    global wall2
    global wall3
    global wall4
    global wall5
    global ball
    global point
    canvas_width = 700
    canvas_height = 400
    w.delete("all")
    w.create_line(0, 200, canvas_width, 200, fill="#400000")
    rect(wall1, w)
    rect(wall2, w)
    rect(wall3, w)
    rect(wall4, w)
    rect(wall5, w)
    circle(ball, w)
    w.create_text(40, 40, text=f'POINTS -->> {point}')
    logic()
    print(point)

    if end == 0:
        w.after(30, display)
    elif end == 1:
        endfunct(w)

def game():                 # main game function
    global w
    master = Tk()

    canvas_width = 700
    canvas_height = 400
    w = Canvas(master,
               width=canvas_width,
               height=canvas_height)
    display()
    w.after(100, display)
    w.pack()
    mainloop()

game()
