# Split string method
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# print(names)
nameval=len(names)
random_choice = random.randint(0, nameval -1 )
person_who_will_pay = names[random_choice]
# print(random_choice)
print(person_who_will_pay + " is picking up the tab")


