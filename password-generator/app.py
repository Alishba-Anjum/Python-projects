import random
import string

def generate_password(length=12, use_digits=True, use_special_chars=True):
    letters = string.ascii_letters  # Upper and lowercase letters
    digits = string.digits if use_digits else ''
    special_chars = string.punctuation if use_special_chars else ''

    all_chars = letters + digits + special_chars
    if not all_chars:
        raise ValueError("At least one character type must be selected")

    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

# User input for password length
try:
    length = int(input("Enter desired password length: "))
    if length <= 0:
        raise ValueError
except ValueError:
    print("Invalid input. Using default length of 12.")
    length = 12

# Generate and display password
password = generate_password(length)
print(f"Generated Password: {password}")
