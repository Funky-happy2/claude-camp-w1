while True:
    #Introduce the program
    print("Welcome to the Tip Calculator!") 

    #Find the meal cost and tip percentage from the user.
    meal_cost = input("Enter the meal cost: ")
    tip_percentage = input("Enter the tip percentage: ")

    #Clean up the strings and turn them into evals
    meal_cost = "".join([char for char in meal_cost if char.isdigit() or char == "."])
    meal_cost = meal_cost.strip()
    meal_cost = eval(meal_cost)

    tip_percentage = "".join([char for char in tip_percentage if char.isdigit() or char == "."])
    tip_percentage = tip_percentage.strip()
    tip_percentage = eval(tip_percentage)

    #Calculate the tip amount and total cost, and print the results.
    tip_amount = meal_cost * (tip_percentage / 100)
    total_cost = meal_cost + tip_amount
    print(f"Tip amount: ${tip_amount:.2f}")
    print(f"Total cost: ${total_cost:.2f}")

    #Ask the user if they want to calculate another tip.
    again = input("Do you want to calculate another tip? (yes/no): ")
    if again.lower() == "no":
        print("Goodbye!")
        break
    elif again.lower() == "yes":
        print("Ok, let's calculate another tip!")
    else:
        print("Invalid input. Let's calculate another tip!")