"""Use the range function to print the numbers from 40 to 1 (backwards)"""
for i in range (40, 0, -1):
    print(i)


"""Repeat the exercise but count by 5's"""
for i in range(40, 0, -5):
    print(i)


"""Write a program that will count print all the multiples of (n) where n is
taken from user input.  Include necessary print statements."""
print('Please type in a number to recieve multiples')
num = int(input())
for i in range(11):
    print(num*i)
