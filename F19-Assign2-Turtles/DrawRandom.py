'''
DrawRandom.py

@author: YJH3 Jenny Huang
'''

import turtle, BoundingBox
import TurtleShapes
import random


def drawEverywhere(turt, func):
    """
    User chooses shape function and number of shapes.
    
    Draws the shape chosen by the user at random locations 
    and random sizes across the screen.
    """
    
    num = input("number of elements> ") #prompts entering in console. type 'string'
    num = int(num)
    WIDTH = 1000
    HEIGHT = 500

    for _ in range(num):
        size = random.randint(50, 100)
        
        turt.penup() #penup when setting the position

            
        x = random.randint(-WIDTH//2, WIDTH//2) #the origin is (0,0)
        y = random.randint(-HEIGHT//2, HEIGHT//2)
    
        turt.setposition(x,y) 
        
        turt.pendown()
        
        func(turt, size)
           
        
        

if __name__ == '__main__':
    win = turtle.Screen()
    BoundingBox.drawBoundingBox()
    funcNumber = input("Input 0 for drawOneShape, 1 for drawOneArrow")
    turt = turtle.Turtle()
    if funcNumber == "0":
        drawEverywhere(turt, TurtleShapes.drawOneShape)
    else:
        drawEverywhere(turt, TurtleShapes.drawOneArrow)
    win.exitonclick()
    