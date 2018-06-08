from random import randint

inp = input('Guess the number: ')
ran = randint(1, 10)

if ran == int(inp):
    print('Correct!')
else:
    print('Wrong, try again!')
