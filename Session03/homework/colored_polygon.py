from turtle import *

n = int(input("Enter n, n < 9: "))

color_list = ['red', 'blue', 'orange', 'yellow', 'grey']
m = -1
if n < 9 :
    for n in range(3, n):
        m += 1
        turtle_color = color_list[m]
        color(turtle_color)
        for _ in range(n):
            forward(100)
            left(360/n)
else:
    print("Only n < 9 is available yet.")
mainloop()
