while True:
    #Import the random module to generate a random greeting.
    import random

    #Get the user's name and age.
    name = input("Enter your name: ")
    age = (input("Enter your age: "))

    #Clean up the age string and turn it into a float.
    age = "".join([char for char in age if char.isdigit()])
    age = age.strip()
    age = float(age)

    #Clean up the name string.
    name = name.strip()

    #Define different greeting functions.
    def greet_formal(name):
        print(f"So, {name}, you're {age} years old. That must mean you were born in {2026 - age}. How nice.")

    def greet_casual(name):
        print(f"Hey {name}! Nice to meet you. I see you're {age} years old. That's pretty cool!")

    def greet_enthusiastic(name):
        print(f"HELLO {name}!!! I CAN'T BELIEVE YOU'RE {age} YEARS OLD! THAT'S AMAZING!!!")

    #Create a list of the greeting functions and randomly choose one to greet the user.
    greetings = [greet_formal, greet_casual, greet_enthusiastic]

    #Randomly choose a greeting function and call it with the user's name.
    chosen = random.choice(greetings)
    print("Generating your greeting...")
    chosen(name)

    #Ask the user if they want to generate another greeting.
    again = input("Do you want to generate another greeting? (yes/no): ")
    if again.lower() == "no":
        print("Goodbye!")
        break
    elif again.lower() == "yes":
        print("Ok, let's generate another greeting!")
    else:
        print("Invalid input. Let's generate another greeting!")

