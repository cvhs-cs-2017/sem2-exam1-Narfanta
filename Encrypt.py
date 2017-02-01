"""Write a code that will remove vowels from a string and run it for the sentence:

'Computer Science Makes the World go round but it doesn't make the world round itself!'

Print the save the result as the variable = NoVowels
"""
def stripvowel(phrase):
    new = ''
    for i in phrase:
        if i == 'a' or i == 'A' or i == 'e' or i == 'E' or i == 'o' or i == 'O' or i == 'u' or i == 'U':
            new = new
        else:
            new = new + i
    return new
print(stripvowel('Computer Science Makes the World go round but it doesn\'t make the world round itself!'))



"""Write an encryption code that you make up and run it for the variable NoVowels"""
