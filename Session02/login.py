print("Hi there, this is a superuser gateway")

while True:
    n = input("Username: ")
    if n.lower() == "c4e":
        m = input("Password: ")
        if m.lower() == "codethechange":
            print("Welcome,c4e")
        else :
            print("Password is incorrect")
    else :
        print("You are not the superuser")
