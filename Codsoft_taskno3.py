# Advanced Password Generator
# Made using Python

import random
import string

print("==== Password Generator ====")

# Step 1: Ask user for password length
while True:
    try:
        length = int(input("Enter desired password length: "))
        if length <= 0:
            print("⚠ Please enter a positive number.")
        else:
            break
    except ValueError:
        print("⚠ Please enter a valid number.")

# Step 2: Ask for complexity options
include_letters = input("Include letters? (y/n): ").lower() == 'y'
include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

# Step 3: Build character pool
characters = ""
if include_letters:
    characters += string.ascii_letters
if include_numbers:
    characters += string.digits
if include_symbols:
    characters += string.punctuation

# Ensure there’s at least one character type
if not characters:
    print("\n⚠ You must select at least one character type! Defaulting to letters and numbers.")
    characters = string.ascii_letters + string.digits

# Step 4: Generate password
password = ''.join(random.choice(characters) for _ in range(length))

# Step 5: Display generated password
print("\n✅ Generated Password:", password)
