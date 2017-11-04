menu = ['10', '22', '33', '47']
print(*menu, sep= ', ')

m = input("Remove 1 number : ")

if m in menu :
    menu.remove(m)
    print(*menu, sep = ', ')
else :
    print(m,"is not inlcluded in the list")
