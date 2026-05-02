
import random


length = int(input("Enter the length of the password: "))
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
password = "".join(random.choice(characters) for _ in range(length))
print(f"Generated password: {password}")