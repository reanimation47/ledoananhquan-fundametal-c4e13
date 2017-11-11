prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

for _ in range(len(prices)):
    M= list(prices.values())
    m = list(prices)
    L = list(stock.values())
    l = list(stock)
    print(l[_], end = ': ')
    print(L[_])
    print('price: ', end = ': ')
    print(M[_])
    print()

total = 0

for s in range(len(prices)):
    q = M[s] * L[s]
    total += q
print("After selling all of my food, i'd make: ",total)
