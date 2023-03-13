#import needed libraries   
import turtle
from turtle import *
import random

#Define constants
RIGHT_EDGE= 400
LEFT_EDGE = -400
BOTTOM_EDGE = -400
TOP_EDGE = 400

GRAVITY = .1
DAMPING = .8
FRICTION = .02

colorList=['chocolate','skyblue','yellow','brown','blue','red']

#This function will update the location of the ball
def moveBall():
    global xVel, yVel

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
    if (x >= RIGHT_EDGE):
        xVel *= -1
        newColorSide=random.randint(2,5)
        ball.color(colorList[newColorSide])
        if xVel!=0:
            ball.setx(x + xVel-5)

    if (x <= LEFT_EDGE):
        xVel *= -1
        newColorSide=random.randint(2,5)
        ball.color(colorList[newColorSide])
        if xVel!=0:
            ball.setx(x + xVel+5)
   
    if (y <= BOTTOM_EDGE+5):
        yVel *= -1
        newColorTopBottom=random.randint(0,2)
        ball.color(colorList[newColorTopBottom])
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

#Define initial position and speed of the ball
ball.setx(100)
ball.sety(200)
xVel = 5
yVel = 3

screen.tracer(0) #turn off auto screen updates to make it faster


while True:
    moveBall()
    screen.update()
