char = input("Enter a single alphabet: ")
if char.isalpha() and len(char) == 1:
 ascii_value = ord(char)
 print(f"The ASCII value of '{char}' is {ascii_value}")
else:
 print("Please enter only one alphabet character.")