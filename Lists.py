
numbers = [i for i in range(1, 11)]
squares = [i**2 for i in numbers]
even_numbers = [i for i in numbers if i % 2 == 0]
odd_squares = [i**2 for i in numbers if i % 2 != 0]
print("Original List:", numbers)
print("Squares:", squares)
print("Even Numbers:", even_numbers)
print("Squares of Odd Numbers:", odd_squares)