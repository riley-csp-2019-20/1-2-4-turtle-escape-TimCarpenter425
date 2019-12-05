import turtle as trtl
import random as rndm
mt = trtl.Turtle(visible = False)
mt.speed(0)
mt.seth(270)
mt.pensize(5)

# walls = 27
walls = 27
# length = 20
length = 20
width = length*2
for i in range(walls):
    if length >= 80 and length <= 460:
        door_distance = 4
        # wall_distance = 10
        wall_length = 30
        wall_distance = rndm.randint(0, length - 10)
        mt.fd(wall_distance)
        mt.right(90)
        mt.fd(width)
        mt.back(width)
        mt.left(90)
        # mt.fd(door_distance)
        mt.penup()
        mt.fd(wall_length)
        mt.pendown()
        mt.fd(length - (wall_distance + door_distance + wall_length))
    else:
        mt.fd(length)
    mt.left(90)
    length += 20
    # print(length)

wn = trtl.Screen()
wn.mainloop()
