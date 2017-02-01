import turtle
sven = turtle.Turtle()
# AddTen(n):  Adds 10 to the parameter n and returns the result
def AddTen(n):
    x = n + 10
    return x
#DrawRectangle(Anyturtle, l, w):
def DrawRectangle(Anyturtle, l, w):
    for i in range(2):
        Anyturtle.forward(w)
        Anyturtle.right(90)
        Anyturtle.forward(l)
        Anyturtle.right(90)
# DrawPoly(Anyturtle, n):  Will draw a regular polygon with 'n' sides of
  #* You should select the size of the polygon so that it always fits in the screen
def DrawPoly(Anyturtle, n):
    Anyturtle.pu()
    Anyturtle.backward(300)
    Anyturtle.left(90)
    Anyturtle.pd()
    for i in range(n):
        Anyturtle.forward(5)
        Anyturtle.right(360/n)
