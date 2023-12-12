# expenses = [10.10, 20.20, 30.30, 40, 50]
expenses = []
num_expenses = int(input("Enter your # of expenses = "))
for i in range(num_expenses):
    expenses.append(float(input("Enter your expense ")))

total = sum(expenses)
# for expense in expenses:
#     sum = expense + sum

print('You spent $', total, sep='')
