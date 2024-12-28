# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

h=float(height)
w=float(weight)
nh = h**2

# print(h)
# print(w)
# print(nw)
bmi = int(w/nh)
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you are normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you gonna die.")



print(str(bmi))