import random
Mylist = ['orange', 'blue', 'red', 'white']

Answer = (random.choice(Mylist))

l = list(Answer)

s = len(list(Answer))

print("_ "* s)

n = input("Guess? ")

if n in l :
    for i in enumerate(l):
