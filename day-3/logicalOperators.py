print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height > 120:
  print("You can ride!")
  age = int(input("What is your age?: "))
  if age < 12:
      print("Child Tickets are 5$")
      bill = 5
  elif age <=18:
      print("Child Tickets are 7$")
      bill = 7
  elif age >= 45 and age <=55:
      print("Free Tickets boomer!!!")
      bill = 0
  else:
      print("Child Tickets are 12$")
      bill = 12

  photo = input("Would you like a photograph?  Y or N:")
  if photo == "Y" or photo == "y":
    #   bill = bill + 3
    bill += 3 # instead of the line above

  print(f"Your final bill is ${bill}")

else:
  print("Sorry shorty")