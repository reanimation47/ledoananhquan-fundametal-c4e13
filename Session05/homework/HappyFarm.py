n = 5

x1 = 1
x2 = 2
count = 0

while count < n:
    print("Month",count,": ",x1,"pair(s) of rabbit")
    X = x1 + x2
    x1 = x2
    x2 = X
    count += 1
