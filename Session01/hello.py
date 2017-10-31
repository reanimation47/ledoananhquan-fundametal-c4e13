n = input("What's your name?")
yob = int(input("Your year of birth?"))
age = 2017 - yob
print("Hello", n)
print("You're", age )

if age < 10:
    print("Baby")
elif age < 18:
    print("teenager")
else:
    print("adult")
