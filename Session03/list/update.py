menu = ['bun', 'cha', 'com']

for index, item in enumerate(menu):
    print(index + 1,". ", item, sep='')

m = int(input("Position you wanna update: "))
n = input("Replace with: ")

index = m -1

menu[index] = n

for index, item in enumerate(menu):

    print(index + 1,". ", item, sep='')
