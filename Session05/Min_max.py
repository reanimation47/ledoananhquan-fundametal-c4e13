numbers = [1, 7, 8, -10, 5, -180, 20]
print(numbers)

min = numbers[0]
max = numbers[0]

found = -1

for index, number in enumerate(numbers):
    if min > numbers[index]:
        min = number
    else:
        min = min
    if max < numbers[index]:
        max = number
    else:
        max = max

print("Min: ",min)
print("Max: ",max)
