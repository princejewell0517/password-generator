# password_generator.py

import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("Welcome to the Password Generator! 🔑")

while True:
    try:
        length = int(input("Enter password length (minimum 6): "))
        if length < 6:
            print("❌ Password length too short. Try again.")
            continue
        password = generate_password(length)
        print(f"Generated password: {password}")
    except ValueError:
        print("❌ Please enter a valid number.")

    again = input("Generate another password? (y/n): ").lower()
    if again != 'y':
        print("Goodbye! 👋")
        break
