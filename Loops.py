"""Write a program that will add 5 and loop until it reaches a number GREATER
than 100.  It should then spit out the result AND tell the user how many times
it had to add 5 (if any)"""
j = int(input('please type a number'))
w = j
x = 0
for i in range(j, 102, 5):
    x = x + 1
    j = j + 5
print('The number reached was ' + str(n))
print('It took ' + str(x) + ' times to reach a number greater than 100')
"""Write a program that will prompt the user for an input value (n) and double
it IF is an ODD number, triple it if is an EVEN number and do nothing if it is
anything else (like a decimal or a string)"""
x = float(input('Please input a value: '))
if float((x)) % 2 == 0:
    n = int(x)*3
elif float((x)) % 1 == 0:
    n = int(x)*2
else:
    n = 'that is not a number'
print(n)
