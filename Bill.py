bill_amount = float(input("Enter the total bill amount: "))
amount_paid = float(input("Enter the amount paid by the customer: "))
due_amount = bill_amount - amount_paid
if due_amount > 0:
    print("The customer still has to pay:", due_amount)
elif due_amount == 0:
    print("The bill is fully paid. No due amount.")
else:
    print("Extra amount paid:", abs(due_amount))