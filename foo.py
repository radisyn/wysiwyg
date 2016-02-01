import turtle
def draw_square():
    # Setup the window
    window = turtle.Screen()
    window.bgcolor("red")

    # Create a turtle
    mad = turtle.Turtle()
    mad.shape("turtle")
    mad.color("yellow")
    mad.speed(2)

    # Draw the square
    mad.forward(100)
    mad.right(90)
    mad.forward(100)
    mad.right(90)
    mad.forward(100)
    mad.right(90)
    mad.forward(100)
    mad.right(90)

    # Create another turtle
    gilbert = turtle.Turtle()
    gilbert.shape("arrow")
    gilbert.color("blue")

    # Draw a circle
    gilbert.circle(100)

    window.exitonclick()
