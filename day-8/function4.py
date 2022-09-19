#Write your code below this line 👇

def prime_checker(number):
    i=2
    prime_yes = 0
    while number % i != 0:
        i+=1
    if i == number:
        prime_yes = 1
    else:
        prime_yes = 0

    if prime_yes == 1:
        print(f"You have chosen {n}, and it is a Prime Number!")
    else:
        print(f"You have chosen {n}, and it is NOT a Prime Number!")


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)





