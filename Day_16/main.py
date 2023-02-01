# Day 16

# import turtle

# Get the class ( a blueprint) of Turtle form the turtle module
# some_turtle = turtle.Turtle()

# Alternatively you can import Turtle class from the turtle module
# from turtle import Turtle
# then to assign the object, simply use:
# another_turtle = Turtle()

from turtle import Turtle, Screen

skolpadda = Turtle()
skolpadda.shape("turtle")
skolpadda.forward(100)
skolpadda.color("green")

# zolw = Turtle()
# zolw.shape('turtle')
my_screen = Screen()
# print(my_screen.canvheight)
my_screen.exitonclick()
