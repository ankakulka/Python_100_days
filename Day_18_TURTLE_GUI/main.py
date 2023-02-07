from turtle import Turtle, Screen
import heroes

timmy = Turtle()
timmy.shape('turtle')
timmy.color('purple')
# Draw a square using turtle
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)

# draw a dashed line alternating with solid line
# for _ in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# Triangle
# timmy.forward(100)
# timmy.right(120)
# timmy.forward(100)
# timmy.right(60)

# Triangle
for i in range(3):
    timmy.color('red')
    timmy.forward(100)
    timmy.right(120)

# Square
for i in range(4):
    timmy.color('green')
    timmy.left(90)
    timmy.forward(100)

# Pentagon
for i in range(5):
    timmy.color('blue')
    timmy.forward(100)
    timmy.right(72)





















screen  = Screen()
screen.exitonclick()