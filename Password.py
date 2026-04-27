import random
import string
def generate_password(length):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    all_chars = lower + upper + digits
    password_list = [random.choice(all_chars) for _ in range(length)]
    random.shuffle(password_list)
    password = ''.join(password_list)
    return password
length = int(input("Enter password length: "))
password = generate_password(length)
print("Generated Password:", password)