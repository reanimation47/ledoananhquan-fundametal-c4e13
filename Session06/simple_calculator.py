def eval(x, y, o):
    if o == '+' :
        m = x + y
    elif o == '-' :
        m = x - y
    elif o == "*" :
        m = x*y
    elif o == "/" :
        if y == 0:
            m = 'NaN'
        else:
            m = x / y
    return m

x1 = 10
y2 = 5                             #function test
o3 = '+'
r = eval(x1, y2, o3)
print(r)


# x = int(input("x = "))
# o = input("Operation(+,-,*,/) : ")
# y = int(input('y = '))
#
# if o in ['+','-','*','/']:
#     r = eval()
#
#
#     print(r)
# else:
#     print("Operation not available")
