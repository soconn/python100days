print("Welcome to the tip Calculator.")
tBill = input("What was the total bill? $")
pTip = input("What percentage tip would you like to give? 10, 12, or 15?")
fBill = float(tBill)
tPay = fBill + ((int(pTip)/100) * fBill)
tDiners = input("How many people to split the Bill? ")
ePay = float(tPay / int(tDiners))
fPay = round(ePay, 2)

print(f"Each person should pay: ${fPay}")