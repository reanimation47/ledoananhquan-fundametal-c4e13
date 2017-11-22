from turtle import *
def draw_square(L, col):
    for i in range(4):
        shape('turtle')
        color(col)
        forward(L)
        left(90)

for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()
