year = int(input("What year is it?"))
fh = year % 400
oh = year % 100
ey = year % 4

if fh == 0:
    ly = 1
elif oh == 0:
    ly = 0
elif ey == 0:
    ly = 1
else:
    ly = 0

if ly == 1:
    print("It is a leap year, happy Birthday Ray Nagle!")
else:
    print("It is not a leap year, no birthday for you Ray Nagle!")
