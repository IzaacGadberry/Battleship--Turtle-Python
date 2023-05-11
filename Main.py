import turtle as t
from turtle import *
import gamePlay as gp

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Tracks how many times player 1 and 2 won or loss

player1Win=0
player1Loss=0
player2Win=0
player2Loss=0

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Sets Up the Window

r = t.Turtle()
r.hideturtle()
t.speed(0)
wn = t.Screen()
wn.screensize(624,624)
wn.bgcolor("gray")
wnTk = wn.getcanvas().winfo_toplevel()
wnTk.attributes("-fullscreen", True)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Button Set Up

button1 = 0
leftbutt = 0
rightbutt = 0

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Homescreen Fuction

def homescreen():

    # ---------------------------------------------------------------------------------------------------------------------------------------------------------------
    # title and background
    
    t.penup()
    t.hideturtle()
    t.goto(-200,100)
    t.write("BATTLESHIP", font=('04b03', 50, "normal"))
    t.goto(-200,-50)
    t.pendown()
    t.fillcolor("lightgray")
    t.begin_fill()
    
    # ---------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Making the VS. AI Button
    
    for i in range(2):
        t.fd(110)
        t.left(90)
        t.fd(50)
        t.left(90)
    t.end_fill()
    t.penup()
    t.goto(-185,-40)
    t.penup()
    t.write("PVC",font=('04b03',20,'normal'))
    t.goto(75,-50)

    # ---------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Making the PVP button
    
    t.pendown()
    t.begin_fill()
    for i in range(2):
        t.fd(110)
        t.left(90)
        t.fd(50)
        t.left(90)
    t.end_fill()
    
    # ---------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Making the credits 
    
    t.penup()
    t.goto(105,-40)
    t.write("PVP",font=('04b03',20,'normal'))
    t.penup()
    t.goto(-99,-150)
    t.write("BY ANDREW AND IZAAC",font=('04b03',12,'normal'))
    
def buttonclick(x,y):
    global leftbutt
    global rightbutt
    global button1
    if x > -200 and x < -90 and y > -50 and y < 0:
        t.clearscreen()
        button1 = 1
        leftbutt = 1
        PVC()
    if x > 80 and x < 180 and y > -50 and y < 0:
        t.clearscreen()
        button1 = 1
        rightbutt = 1
        PVP()
        
def PVP():
    gp.p()
       
def PVC():
    gp.c()

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------
# All the Functions Run in This One Function

def alwaysrunning():
    homescreen()
    if button1 == 0:
        t.onscreenclick(buttonclick, 1)
        t.listen()
    if rightbutt == 1:
        PVP()
alwaysrunning()


wn.mainloop()
