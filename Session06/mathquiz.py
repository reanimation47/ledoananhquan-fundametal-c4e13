from random import random, randint, choice
from simple_calculator import eval

import random

n = randint(-1, 2)
x = randint(1, 11)
y = randint(1, 11)
op = choice(['+','-','*','/'])


print("*******")

print("{0} {3} {1} = {2}".format(x, y, m, op))

print("*******")

ans = input("(Y/N)?").upper()
#
if x + y + n == eval(x, y, '+') :
    if ans == 'Y':
        print('Yay')
    elif ans == 'N':
        print('Nah')
elif x + y + n != eval(x, y, '+'):
    if ans == 'Y':
        print('Nah')
    elif ans == 'N':
        print('Yay')
