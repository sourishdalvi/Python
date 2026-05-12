string = input("Enter a sentence: ")
words = string.split()
reversed_words = words[::-1]
result = " ".join(reversed_words)
print("Reversed sentence:")
print(result)