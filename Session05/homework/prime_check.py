n = int(input("Enter a number: "))

c = 0

for i in range(2, n):
    if n % i == 0:
        c +=1

if c == 0:
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")
