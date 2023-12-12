# Get the Information
moneyOwed = float(input("How much money do you owe?\n"))
intRate = float(input("How much is annual interest rate?\n"))
payment = float(input("How much will you pay off each month?\n"))
months = int(input("How many months do you want to see results for?\n"))

# monthly interest rate
monthly_intRate = intRate/100/12

for month in range(months):
    # Interest to pay
    interest_paid = moneyOwed * monthly_intRate
    # Add in interest
    moneyOwed = moneyOwed + interest_paid

    if(moneyOwed - payment < 0):
        print("The last payment is", moneyOwed)
        print("You paid off the loan in", month+1, "months")
        break

    # Make Payment
    moneyOwed = moneyOwed - payment

    print("You paid", payment, "of which", interest_paid, "was interest", end=" ")
    print("Now you owe", moneyOwed)
