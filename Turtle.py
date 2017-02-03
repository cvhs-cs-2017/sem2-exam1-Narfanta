import turtle
"""Create a Turtle Program that will draw a 3-dimensional cube"""
cube = turtle.Turtle()
cube.pu()
cube.backward(100)
cube.pd()
for i in range(4):
    cube.forward(20)
    cube.right(90)
cube.left(45)
cube.forward(10)
cube.right(45)
cube.forward(20)
cube.right(135)
cube.forward(10)
cube.speed(0)
cube.backward(10)
cube.speed(1)
cube.left(45)
cube.forward(20)
cube.right(45)
cube.forward(10)
input()
"""Import and Call the DrawRectangle(Anyturtle, l, w) function from the
file MyFile.py"""
