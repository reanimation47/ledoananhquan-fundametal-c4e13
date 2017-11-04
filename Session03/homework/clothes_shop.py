
clothes = ['Jeans', 'Tshirs', 'Shorts','Sweaters' ]
print("Our clothes: ")
for index, item in enumerate(clothes):
    print(index + 1,". ",item, sep='')
n = input("Add new clothes: ")

clothes.insert(0, n)

print("******************")

print("Our updated list: ")

for index, item in enumerate(clothes):
    print(index + 1,". ",item, sep='')

m = int(input("Position needs to be updated: "))
h = input("Replace it with :")

index= m-1

if index < 5:

    clothes[index] = h

    print("************************")

    print("Our updated list: ")
    for index, item in enumerate(clothes):

        print(index + 1,". ",item, sep='')
else:
    print("Not included in the list")

q = int(input("Position needs to be removed: "))

index = q -1

if index <5:

    clothes.remove(clothes[index])

    print("**************")

    print("Our updated list: ")
    for index, item in enumerate(clothes):

        print(index + 1,". ",item, sep='')
else:
    print("Not include in the list")
