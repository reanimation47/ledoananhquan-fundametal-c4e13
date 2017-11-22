from turtle import *

def draw_star(x, y, length):
    hideturtle()
    penup()
    goto(x, y)
    showturtle()
    pendown()
    for m in range(5):
            forward(length)
            right(2*360.0/5)

speed(-1)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
length = random.randint(3, 10)
draw_star(x, y, length)

mainloop()
