a = int(input("Enter a :"))
b = int(input("Enter b :"))
c = int(input("Enter c :"))
if a == 0:
    print("kp ptbac2")
    print("One solution  x=", (- c) / b)
else:
    delta = (b * b) - 4 * a * c
    if delta < 0:
        print("No solution")
    elif delta == 0:
        print("One solution x =", (- b) / (2 * a))
    else:
        x1 = ((-b)+(delta**0.5))/(2*a)
        x2 = ((-b)-(delta**0.5))/(2*a)
        print("Two solutions x1 = {0}, x2 = {1}".format(x1, x2))
