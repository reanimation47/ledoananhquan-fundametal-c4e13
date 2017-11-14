numbers = [1,2,3,4,5,6,7,8,9,2,3,1,4,3,2,4,5,2,3,4,5,2]

print(numbers)

n = int(input("Enter a number: "))

c = 0

for index, items in enumerate(numbers):
    if n == items:
        c +=1

print(c)
