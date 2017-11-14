numbers = [ -5, 1, 7, 10, 12, 13, 23]

x = int(input("Enter n= "))

start = 0
stop = len(numbers)
f = -1

while start != stop:
    mid = (start+stop)//2
    m = numbers[mid]
    if x == m:
        f = mid
        break
    else:
        if mid == start or mid == stop:
            break
        elif x < m:
            stop = mid
        else:
            start = mid

if f == -1:
    print("Not found")
else:
    print("Found at:",f)
