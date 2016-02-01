import turtle
def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")
    mad = turtle.Turtle()
    mad.shape("turtle")
    mad.color("yellow")
    mad.speed(2)

    mad.forward(100)
    mad.right(90)
    mad.forward(100)
    mad.right(90)
    mad.forward(100)
    mad.right(90)
    mad.forward(100)
    mad.right(90)

    gilbert = turtle.Turtle()
    gilbert.shape("arrow")
    gilbert.color("blue")
    gilbert.circle(100)

    window.exitonclick()
