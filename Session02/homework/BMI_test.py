h = int(input("Your height in centimeters: "))
m = int(input("Your weight in kilograms: "))
H = h / 100
bmi = m / ( H * H)
if bmi < 16 :
     print("You are severely underweight")
elif bmi <= 18.5 :
    print("You are underweight")
elif bmi <= 25 :
    print("You are normal")
elif bmi <= 30 :
    print("You are overweight")
else :
    print("You are obese")
