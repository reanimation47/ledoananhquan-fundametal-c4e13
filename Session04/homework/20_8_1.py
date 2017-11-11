m = input("Enter a string: ")
m = m.upper()

L = list(m.upper())



n = {}

for x in m :
    n[x] = n.get(x, 0) + 1

q = list(n.items())
q.sort()
for i in q:
    print(*i)
