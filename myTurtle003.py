#Tera Schaller 7/20/2017
#Udacuty fundamentals of Python tutorial
#Use turtle module to draw a spiral of squares
#Python 3.6.1

import turtle

def draw_square(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def draw_art(turtleShape, bg_color, art_color, size):
    window = turtle.Screen()
    window.bgcolor(bg_color)

    mike = turtle.Turtle()
    mike.shape(turtleShape)
    mike.color(art_color)
    mike.speed(25)

    for j in range(700):
        draw_square(mike, size+j)
        mike.right(5)

    window.exitonclick()
    

draw_art("turtle", "cyan", "blue", 10)
