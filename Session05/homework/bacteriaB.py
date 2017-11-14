n = int(input("How many B bacterias are there?"))

t = int(input("How much time in minutes we will wait?"))

if t % 2 == 0:
    T = t / 2
    x = (2**T)*n
    print("After", t, "minutes,we would have", x, "bacterias" )
else:
    T = (t-1)/2
    x = (2**T)*n
    print("After", t, "minutes,we would have", x, "bacterias" )
