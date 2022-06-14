#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲

import random
quarter = random.randint(0, 1)

if quarter == 1:
    face = "Heads"
else:
    face = "Tails"

print(quarter)
print(face)
