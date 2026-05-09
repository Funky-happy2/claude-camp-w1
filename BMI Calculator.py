while True: 
   #Find the height and weight of user.
    height = (input("Enter your height in cm: "))
    weight = (input("Enter your weight in kg: "))

    #Clean up the string and turn into a float.
    hnum = "".join([char for char in height if char.isdigit()])
    wnum = "".join([char for char in weight if char.isdigit()])
    newh = hnum.strip()
    neww = wnum.strip()
    newh = float(newh)
    neww = float(neww)

    #Calculate BMI and print the result.
    bmi = neww / ((newh / 100) ** 2)
    print(f"Your BMI is: {bmi:.2f}")
    if bmi < 18.5:
        print("You are underweight.")
    elif 18.5 <= bmi < 25:
        print("You have a normal weight.")
    elif 25 <= bmi < 30:
        print("You are overweight.")
    else:
        print("You are obese.")
    
    #Ask the user if they want to calculate again.
    again = input("Do you want to calculate again? (yes/no): ")
    if again.lower() == "no":
        print("Goodbye!")
        break
    elif again.lower() == "yes":
        print("Ok, let's calculate again!")
    else:
        print("Invalid input. Let's calculate again!")
