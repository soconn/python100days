# 🚨 Don't change the code below 👇
print("Welcome to B-Money Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
cost = 0
if size == "S":
    cost = 15
elif size == "M":
    cost = 20
elif size == "L":
    cost = 25
else:  
    print("That isn't a real size dummy!")
    exit

if add_pepperoni == "Y":
    if size == "S":
        cost += 2
    else:
        cost += 3

if extra_cheese == "Y":
    cost += 1

print(f"Please pay ${cost} for your great B-Money Pizza!")
