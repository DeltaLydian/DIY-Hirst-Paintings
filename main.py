import turtle
import turtle as turtle_module
import random
colorlist = [(228, 231, 237), (191, 142, 195), (243, 209, 226), (222, 232, 223), (146, 167, 183), (167, 161, 154), (92, 96, 112), (238, 165, 197), (142, 171, 157), (112, 106, 99), (113, 94, 106), (26, 32, 45), (153, 110, 145), (178, 183, 217), (47, 32, 41)]
screen = turtle_module.Screen()
cursor = turtle_module.Turtle()
turtle_module.colormode(255)

cursor.hideturtle()
cursor.penup()
cursor.setpos(0,0)
cursor.setheading(225)
cursor.forward(300)
cursor.pensize(30)
cursor.speed("fastest")



num_columns = 10
num_rows = 10

for y in range(0, num_rows):
    cursor.setheading(0)
    for x in range(0,num_columns):
        rgb = random.choice(colorlist)
        cursor.pencolor(rgb)
        cursor.dot(30)
        cursor.forward(50)

    cursor.setheading(180)
    cursor.forward(num_columns * 50)
    cursor.setheading(90)
    cursor.forward(50)


screen.exitonclick()