# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

print(name1)
print(name2)

combined_string = name1 + name2

t=combined_string.count("t")
r=combined_string.count("r")
u=combined_string.count("u")
e=combined_string.count("e")

true = t+r+u+e

l=combined_string.count("l")
o=combined_string.count("o")
v=combined_string.count("v")
e=combined_string.count("e")

love=l+o+v+e

score=int(str(true) + str(love))
# print(f"Your score is " + {score})

score = int(score)

if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos!")
elif (score >= 40) and (score <= 50):
    print(f"Your score is {score}, you'll be alright together")
else:
    print(f"Your Score is {score}! You are doomed")
