while True:
    f_or_c = input("Enter F or C: ")
    if f_or_c == "F":
        f = input("Enter the temperature in F: ")
        f = "".join([char for char in f if char.isdigit()])
        f = f.strip()
        f = float(f)
        c = (f - 32) * 5 / 9
        print(f"{f} Fahrenheit is {c:.2f} degrees Celsius to 2 decimal points.")
    elif f_or_c == "C":
        c = input("Enter the temperature in C: ")
        c = "".join([char for char in c if char.isdigit()])
        c = c.strip()
        c = float(c)
        f = (c * 9 / 5) + 32
        print(f"{c} degrees Celsius is {f:.2f} Fahrenheit to 2 decimal points.")
    else:
        print("Invalid input. Please enter F or C.")

    #Ask the user if they want to convert another temperature.
    again = input("Do you want to convert another temperature? (yes/no): ")
    if again.lower() == "no":
        print("Goodbye!")
        break
    elif again.lower() == "yes":
        print("Ok, let's convert another temperature!")
    else:
        print("Invalid input. Let's convert another temperature!")
        