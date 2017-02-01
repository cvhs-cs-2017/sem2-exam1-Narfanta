import turtle
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
