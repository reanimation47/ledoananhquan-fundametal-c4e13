menu = ['chan ga sa ot', 'ga xao pho mai', 'com rang dua bo']
print(*menu, sep=', ')

n = input("Add one more ?")

menu.insert(0, n)
print(*menu, sep=', ')
