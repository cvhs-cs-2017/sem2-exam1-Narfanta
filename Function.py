"""Define a function that will take a parameter, n, and triple it and return
the result"""
def Triple(n):
    x = n*3
    return x
print(Triple(5))

"""Write a program that will prompt the user for an input value (n) and print
the result of 3n by calling the function defined above.  Make sure you include
the necessary print statements and address any issues with whitespace. """
print('Please type in a NUMBER to triple.')
x = int(input())
print(Triple(x))
