row = int(input("Rows = "))
column = int(input("Columns = "))

for y in range(row):
    for x in range(column):
        if (x + y) % 2 ==0:
            print("x", end ='')
        else:
            print("*",end ='')
    print()
