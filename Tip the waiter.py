total_bill = float(input("What was the total bill? "))
tip_percent = int(input("What percentage tip would you like to give? "))
tip_amount = (tip_percent / 100) * total_bill
final_amount = total_bill + tip_amount
print(f"You should tip ${tip_amount:.2f}.")
print(f"The final amount is ${final_amount:.2f}.")