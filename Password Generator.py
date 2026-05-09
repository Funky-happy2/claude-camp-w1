while True:
    #Introduce the program
    print("Welcome to the Password Generator!")
    #Import the random module to generate a random password.
    import random

    #Get the desired length of the password from the user.
    length = (input("Enter the length of the password: "))

    #Clean up the string and turn it into an integer.
    length = "".join([char for char in length if char.isdigit()])
    length = length.strip()
    length = int(length)

    #Define the characters that can be used in the password and generate a random password.
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

    #Generate a random password of the desired length and print it.
    password = "".join(random.choice(characters) for _ in range(length))
    print(f"Generated password: {password}")

    #Ask the user if they want to generate another password.
    again = input("Do you want to generate another password? (yes/no): ")
    if again.lower() == "no":
        print("Goodbye!")
        break
    elif again.lower() == "yes":
        print("Ok, let's generate another password!")
    else:
        print("Invalid input. Let's generate another password!")