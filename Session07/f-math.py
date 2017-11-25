from random import *
from simple_calculator import eval
def generate_quiz():
    x = randint(1, 10)
    y = randint(1, 10)
    error = randint(-1,1)
    op = choice(['+','-','*','/'])
    return [x, y, op, eval(x,y,op)+ error]

def check_answer(x, y, op, result, user_choice):
    true_result = eval(x, y, op)
    if user_choice:
        return true_result == result
    else:
        return true_result != result
