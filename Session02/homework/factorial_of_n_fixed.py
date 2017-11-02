from math import factorial

n = int(input("Enter n: "))

if n >= 0 :
    f = factorial(n)

    print("Factorial of n = ", f)


else :
    print("Factorials do not exist for negative numbers")
