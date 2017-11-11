
teen_dict = {
    'ik': 'Đi(v).',
    'ng': 'Người(n)',
    'r': 'Rồi',
    's': 'Sao',
    'kb': 'Không biết',
}
while True:
    print("Our list of codes :")
    print()
    print(teen_dict)
    m = input("Your code? :")

    if m in teen_dict:
        print(teen_dict[m])
    else:

        n = input("Not found, do you want to contribute this word? (Y/N)").upper()

        if n == 'Y' :
            nw = input("Translation : ")
            teen_dict[m] = nw
            print("Updated")
        else:
            print("Ok")
