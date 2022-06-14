import random
import myModule

random_randint = random.randint(1, 100)
print(random_randint)

random_float = random.random()
print(random_float)

print(myModule.pi)
random5 = random.randint(0, 4) + random_float
print(f"Random number between 0 and 5: {random5}")

love_score = random.randint(1, 100)
print(f"Your Love score is {love_score}")
