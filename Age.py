try:
 age = int(input("Enter your age: "))
 if age < 0:
  print("Error: Age cannot be negative.")
 elif age > 120:
  print("Error: Age seems unrealistic.")
 else:
  print("Valid age entered.")
 if age % 2 == 0:
  print("The age is even.")
 else:
  print("The age is odd.")
except ValueError:
    print("Error: Please enter a valid number.")