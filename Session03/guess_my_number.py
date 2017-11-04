from random import randint

n = randint(0, 101)

count = 0

while True:

    m = int(input("Guess the number,you can only guess 7 times ? "))

    if m == n :
        print("Bingo")
        break
    if m > n :
        print("Too large")
        count +=1
    else :
        print("Too small")
        count += 1
    if count >8 :
        print("Out of guesses")
        break
