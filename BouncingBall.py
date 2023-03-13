#changelog:
#Q1:randomize ball color when it hits the right or left wall, use a different set of colors for the floor and ceiling, but still randomize.
#Q2:change screen size from 400x400 to 175x175 by pressing the Up key (up arrow)
#Q3:ball increases in speed by 5 every 3 bounces (on any surface.) - note: messing with a combination of this feature and the screen resize feature causes some weird and interesting bugs that i don't quite understand.

#import needed libraries   
import turtle
from turtle import *
import random

#Define constants
RIGHT_EDGE= 400
LEFT_EDGE = -400
BOTTOM_EDGE = -400
TOP_EDGE = 400

RIGHT_EDGE2 = 175
LEFT_EDGE2 = -175
BOTTOM_EDGE2 = -175
TOP_EDGE2 = 175

GRAVITY = .1
DAMPING = .8
FRICTION = .02

colorList=['chocolate','skyblue','yellow','brown','blue','red']

#know whether or not to use 400x400 (OG) screen or 175x175
useOGscreen=True

#counts number of times ball hits wall up to 3
ballCounter=0

#This function will update the location of the ball
def moveBall():
    global xVel, yVel, ballCounter

    #update the postiion of the ball
    x = ball.xcor()
    if xVel != 0: # we have not stopped rolling due to friction
        ball.setx(x + xVel)
        
    y = ball.ycor()
    if yVel!=0: #if it's 0 we are not bouncing, we are rolling
        yVel = yVel - GRAVITY   #only y is impacted by gravity
        ball.sety(y + yVel)
    else:   # friction comes into play while rolling which impacts xVel
        if (xVel>0):  xVel = xVel-FRICTION
        if (xVel<0):  xVel = xVel+FRICTION
        if abs(xVel)>.005:  #we are still rolling
            # print(xVel) - debug
            pass
        else:  # we are done - ball stopped bouncing and then stopped rolling
            exit()

    #Check for collisons and reverse the direction if so
    if useOGscreen==True:
        if (x >= RIGHT_EDGE):
            xVel *= -1
            newColorSide=random.randint(2,5)
            ball.color(colorList[newColorSide])
            ballCounter=ballCounter+1
            if xVel!=0:
                ball.setx(x + xVel-5)

        if (x <= LEFT_EDGE):
            xVel *= -1
            newColorSide=random.randint(2,5)
            ball.color(colorList[newColorSide])
            ballCounter=ballCounter+1
            if xVel!=0:
                ball.setx(x + xVel+5)
       
        if (y <= BOTTOM_EDGE+5):
            yVel *= -1
            newColorTopBottom=random.randint(0,2)
            ball.color(colorList[newColorTopBottom])
            ballCounter=ballCounter+1
            yVel = yVel * DAMPING #damping effect
            if yVel>2:
                ball.sety(y + yVel+5)
            else:
                yVel=0

        if (y >= TOP_EDGE):
            yVel *= -1
            newColorTopBottom=random.randint(0,2)
            ball.color(colorList[newColorTopBottom])
            ball.sety(y + yVel-5)
    else:
        if (x >= RIGHT_EDGE2):
            xVel *= -1
            newColorSide=random.randint(2,5)
            ball.color(colorList[newColorSide])
            ballCounter=ballCounter+1
            if xVel!=0:
                ball.setx(x + xVel-5)

        if (x <= LEFT_EDGE2):
            xVel *= -1
            newColorSide=random.randint(2,5)
            ball.color(colorList[newColorSide])
            ballCounter=ballCounter+1
            if xVel!=0:
                ball.setx(x + xVel+5)
       
        if (y <= BOTTOM_EDGE2+5):
            yVel *= -1
            newColorTopBottom=random.randint(0,2)
            ball.color(colorList[newColorTopBottom])
            ballCounter=ballCounter+1
            yVel = yVel * DAMPING #damping effect
            if yVel>2:
                ball.sety(y + yVel+5)
            else:
                yVel=0

        if (y >= TOP_EDGE2):
            yVel *= -1
            newColorTopBottom=random.randint(0,2)
            ball.color(colorList[newColorTopBottom])
            ballCounter=ballCounter+1
            ball.sety(y + yVel-5)

#increases ball speed every three times it hits any of the 4 edges
def increase_speed():
    global xVel,ballCounter
    if ballCounter>=3:
        xVel=xVel+5
        ballCounter=0

#resizes screen
def screen_resize():
    global RIGHT_EDGE,LEFT_EDGE,BOTTOM_EDGE,TOP_EDGE,RIGHT_EDGE2,LEFT_EDGE2,BOTTOM_EDGE2,TOP_EDGE2,useOGscreen
    if useOGscreen==True:
        useOGscreen=False
    elif useOGscreen==False:
        useOGscreen=True
    

#Global variables
screen = Screen()
screen.title("My window")
screen.bgcolor("green")

ball = Turtle()
ball.clear()
ball.penup()

ball.shape("circle")
ball.color("blue")
ball.position()
ball.speed(0)
ball.setheading(40)

#keybinds
screen.listen()
turtle.onkey(screen_resize,'Up')

#Define initial position and speed of the ball
ball.setx(100)
ball.sety(200)
xVel = 5
yVel = 3

screen.tracer(0) #turn off auto screen updates to make it faster

while True:
    moveBall()
    increase_speed()
    screen.update()
   
