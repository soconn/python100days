age = input("What is your current Age: ")

total = 90
year = int(total - int(age))
months = int(year * 12)
weeks = int(year  * 52)
days = float(year * 365.25)

print(f"You have {days} days, {weeks} weeks, {months} months, or {year} years!")