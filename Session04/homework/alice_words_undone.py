
sd = open('alice.txt','r')


n = {}

for x in sd:
    n[x] = n.get(x, 0) + 1
