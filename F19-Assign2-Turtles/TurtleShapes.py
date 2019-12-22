'''
TurtleShapes.py

@author: YJH3 JENNY HUANG
'''

import turtle, BoundingBox

def drawOneShape(turt, size2):
    """
    Creates a square of the specified size.
    """
    for i in range(4):
        turt.forward(size2)
        turt.right(90)
        turt.speed(10)

def drawOneArrow(turt, size): #how to specify size when you have many different sized lines. What does it mean by two shapes? good way to change colors?
    """
    Creates an arrow of a specified size.
    """
    
    for i in range(1):
        turt.color("red")
        turt.forward(size*2)
        turt.right(90)
        turt.color("blue")
        turt.forward(size)
        turt.right(90)
        turt.color("green")
        turt.forward(size*2)
        turt.left(90)
        turt.forward(size/4)
        turt.right(120)
        turt.forward(size*1.5) #calculate
        turt.right(120)
        turt.color("red")
        turt.forward(size*1.5) #calculate
        turt.color("blue")
        turt.right(120)
        turt.forward(size*1.5)
        turt.left(90)
        



if __name__ == '__main__':
    win = turtle.Screen()
    BoundingBox.drawBoundingBox()
    turt = turtle.Turtle()
    size2 = 125
    size = 80
    drawOneShape(turt, size2)
    turt.penup()
    x = 150
    y = -150
    turt.setposition(x,y) 
    turt.pendown()
    drawOneArrow(turt, size)
    win.exitonclick()
    