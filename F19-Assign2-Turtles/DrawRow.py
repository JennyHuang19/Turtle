'''
DrawRow.py

@author: YJH3 JENNY HUANG 
'''

import turtle, BoundingBox
import TurtleShapes
import random

def drawRowsOfRows(turt, func):
    """
    Draws ten rows of the shape specified in func across the screen, 
    with each row at a different y-coordinate. The rows have ten shapes 
    in each row, and the shapes in a given row are all 
    the same size and y-coordinate.
    """
    lst = [] #random sizes 
    lstZ = [] #random Y coordinates
    while len(lst)<20: #creating a list with 20 random sizes
        randomSize = random.randint(5,30)
        if randomSize not in lst:
            lst.append(randomSize)
            
    while len(lstZ)<20: #creating a list with 20 random positions
        randomPosition = random.randint(-250,250)
        if randomPosition not in lstZ:
            lstZ.append(randomPosition) 
    
    
    for i in range(10):
        size = lst[i]
        y = lstZ[i] #position of y coordinate varies.
        x = -200 #always start at a set position x.
        for i in range(10): #drawing the func 10 times, each 50 to the right.
            turt.speed(20)
            turt.penup()
            turt.setposition(x,y)
            x=x+50
            turt.pendown()
            func(turt,size)
            



if __name__ == '__main__':
    win = turtle.Screen()
    BoundingBox.drawBoundingBox()
    turt = turtle.Turtle()
    
    drawRowsOfRows(turt,TurtleShapes.drawOneArrow)
    win.exitonclick()
    