import random

name = input("Enter your name: ")
age = int(input("Enter your age: "))

def greet_formal(name):
    print(f"So, {name}, you're {age} years old. That must mean you were born in {2026 - age}. How nice.")

def greet_casual(name):
    print(f"Hey {name}! Nice to meet you. I see you're {age} years old. That's pretty cool!")

def greet_enthusiastic(name):
    print(f"HELLO {name}!!! I CAN'T BELIEVE YOU'RE {age} YEARS OLD! THAT'S AMAZING!!!")

greetings = [greet_formal, greet_casual, greet_enthusiastic]

chosen = random.choice(greetings)
print("Generating your greeting...")
chosen(name)

