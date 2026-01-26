num = int(input("Enter a decimal number: "))
binary = ""
while num > 0:               
    remainder = num % 2
    count = 0
    while count < 1:          
        binary = str(remainder) + binary
        count += 1
    num = num // 2
print("Binary equivalent:", binary)