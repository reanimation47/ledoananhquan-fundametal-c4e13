from turtle import *

n = int(input("Enter n= "))
for n in range(3, n):
    if n % 2 == 0:
        color('red')
    else :
        color('blue')
    for _ in range(n):
        forward(100)
        left(360 / n)

mainloop()
