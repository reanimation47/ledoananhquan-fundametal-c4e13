numbers = [0, -5, 10, 6, 8]

x = int(input("Enter number : "))

found_index = -1

for index,number in enumerate(numbers):
    if x == number:
        found_index = index
        break

if found_index == -1:
    print("Not found")
else:
    print("Found",number,"at",found_index)
