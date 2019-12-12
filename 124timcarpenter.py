import turtle as trtl
import random as rndm

#initialize maze turtle (mt)
mt = trtl.Turtle(visible = False)
mt.speed(0)
mt._delay(0)
mt.seth(270)
mt.pensize(5)

#make prize
prize = trtl.Turtle(shape = "square")
prize.color("red")
prize.pencolor("black")
prize.penup()
prize.goto(20, 0)
prize.shapesize(0.6)

def drawDoor():
    global wall_length
    mt.penup()
    mt.fd(wall_length)
    mt.pendown()

def drawWall():
    global wall_distance
    global width
    mt.fd(wall_distance)
    mt.right(90)
    mt.fd(width)
    mt.back(width)
    mt.left(90)

score = 0

def moveForward():
    global font_setup
    global score
    if (nt.xcor() - prize.xcor()) <= 10 and (nt.xcor() - prize.xcor()) >= -10:
        if (nt.ycor() - prize.ycor()) <= 10 and (nt.ycor() - prize.ycor()) >= -10:
            nt.penup()
            nt.goto(258, 250)
            nt.seth(270)
            nt.clear()
            nt.pendown()
            score += 1
            mt.penup()
            mt.goto(-25, 300)
            mt.clear()
            mt.write(score, font=font_setup)
            mt.goto(0, 0)
            mt.pendown()
            mt.seth(270)
            drawMaze()
        else:
            pass
    else:
        pass
    nt.fd(5)
def moveBack():
    global score
    global font_setup
    if (nt.xcor() - prize.xcor()) <= 10 and (nt.xcor() - prize.xcor()) >= -10:
        if (nt.ycor() - prize.ycor()) <= 10 and (nt.ycor() - prize.ycor()) >= -10:
            nt.penup()
            nt.goto(258, 250)
            nt.seth(270)
            nt.clear()
            nt.pendown()
            score += 1
            mt.penup()
            mt.goto(-25, 300)
            mt.clear()
            mt.write(score, font=font_setup)
            mt.goto(0, 0)
            mt.pendown()
            mt.seth(270)
            drawMaze()
        else:
            pass
    else:
        pass
    nt.fd(-5)
def turnLeft():
    nt.left(90)
def turnRight():
    nt.right(90)

def drawMaze():
    global wall_distance
    global wall_length
    global width
    #define variables
    walls = 27
    length = 20
    width = length*2
    #for each wall:
    for i in range(walls):
        #not the first 4 and not the last 4
        if length >= 80 and length <= 460:
            #define variables
            door_distance = 4
            wall_length = 40
            wall_distance = rndm.randint(0, length - 10)
            #draw wall and barrier
            drawWall()
            drawDoor()
            #finish side
            mt.fd(length - (wall_distance + door_distance + wall_length))
        else:
            mt.fd(length)
        mt.left(90)
        length += 20
drawMaze()

# initialize navigator turtle (nt)
nt = trtl.Turtle()
nt._delay(0)
nt.penup()
nt.seth(270)
nt.goto(258, 250)
nt.pendown()
nt.pensize(2)
nt.shapesize(1.5)
nt.color("black")
nt.pencolor("red")

wn = trtl.Screen()

wn.onkeypress(moveForward, "w")
wn.onkeypress(turnLeft, "a")
wn.onkeypress(turnRight, "d")
wn.onkeypress(moveBack, "s")
wn.onkeypress(moveForward, "Up")
wn.onkeypress(turnLeft, "Left")
wn.onkeypress(turnRight, "Right")
wn.onkeypress(moveBack, "Down")
wn.listen()

font_setup = ("Impact", 40, "normal")

wn.mainloop()
