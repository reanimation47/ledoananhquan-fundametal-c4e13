from turtle import *

color_list = ['red', 'blue', 'orange', 'yellow', 'grey']

q = -1


n = int(input("Enter number of shapes: "))

m = n * 4
if n < 6:
    for i in range(n):
        q +=1
        colored = color_list[q]

        begin_fill()
        forward(20)
        left(90)
        forward(100)
        left(90)
        forward(20)
        left(90)
        forward(100)
        left(90)
        forward(20)
        color(colored)
        end_fill()

else:
    print("Only less than 6 is available yet")

mainloop()
