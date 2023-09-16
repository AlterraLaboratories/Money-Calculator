import os

# Function to calculate the total value of Euro bills and coins.
def calceuro():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen (Windows: 'cls', Unix: 'clear')
    print("Euro Money Calculator")  # Display a title for the Euro calculator.
    print("Enter the number of each Euro bill/coin denomination:")  # Prompt the user to input the number of each Euro denomination.
    
    try:
        # Input the quantity of each Euro bill/coin denomination.
        one = int(input("Number of €1 coins: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        two = int(input("Number of €2 coins: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        five = int(input("Number of €5 bills: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        ten = int(input("Number of €10 bills: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        twenty = int(input("Number of €20 bills: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        fifty = int(input("Number of €50 bills: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        hundred = int(input("Number of €100 bills: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        two_hundred = int(input("Number of €200 bills: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        five_hundred = int(input("Number of €500 bills: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        calceuro()  # Call the function again to re-enter Euro values if there's invalid input.

    # Calculate the total amount in Euros based on user input.
    total_euro = (one * 1) + (two * 2) + (five * 5) + (ten * 10) + \
                (twenty * 20) + (fifty * 50) + (hundred * 100) + \
                (two_hundred * 200) + (five_hundred * 500)
    
    # Display the total amount in Euros with 2 decimal places.
    print(f"\nTotal amount in Euros: €{total_euro:.2f}")

# Function to calculate the total value of Dollar bills.
def calcdollar():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
    print("Dollar Money Calculator")  # Display a title for the Dollar calculator.
    print("Enter the number of each Dollar Bill denomination:")  # Prompt the user to input the number of each Dollar denomination.
    
    try:
        # Input the quantity of each Dollar bill denomination.
        one = int(input("Number of $1 bills: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        two = int(input("Number of $2 bills: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        five = int(input("Number of $5 bills: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        ten = int(input("Number of $10 bills: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        twenty = int(input("Number of $20 bills: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        fifty = int(input("Number of $50 bills: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        hundred = int(input("Number of $100 bills: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        calcdollar()  # Call the function again to re-enter Dollar values if there's invalid input.

    # Calculate the total amount in Dollars based on user input.
    total_dollar = (one * 1) + (two * 2) + (five * 5) + (ten * 10) + \
                (twenty * 20) + (fifty * 50) + (hundred * 100)
    
    # Display the total amount in Dollars with 2 decimal places.
    print(f"\nTotal amount in Dollars: ${total_dollar:.2f}")

# Function to calculate the total value of Canadian Dollar bills and coins.
def calccaddollar():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
    print("Canadian Dollar Money Calculator")  # Display a title for the Canadian Dollar calculator.
    print("Enter the number of each Canadian Dollar Bill/Coin denomination:")  # Prompt the user to input the number of each Canadian Dollar denomination.
    
    try:
        # Input the quantity of each Canadian Dollar bill/coin denomination.
        nickel = int(input("Number of 5 cent coins: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        dime = int(input("Number of 10 cent coins: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        quarter = int(input("Number of 25 cent coins: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        fifty_cent = int(input("Number of 50 cent coins: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        one = int(input("Number of $1 coins: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        two = int(input("Number of $2 coins: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        five = int(input("Number of $5 bills: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        ten = int(input("Number of $10 bills: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        twenty = int(input("Number of $20 bills: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        fifty = int(input("Number of $50 bills: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        hundred = int(input("Number of $100 bills: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        calccaddollar()  # Call the function again to re-enter Canadian Dollar values if there's invalid input.

    # Calculate the total amount in Canadian Dollars based on user input.
    total_dollar = (nickel * 0.05) + (dime * 0.10) + (quarter * 0.25) + (fifty_cent * 0.50) + \
                   (one * 1) + (two * 2) + (five * 5) + (ten * 10) + \
                   (twenty * 20) + (fifty * 50) + (hundred * 100)
    
    # Display the total amount in Canadian Dollars with 2 decimal places.
    print(f"\nTotal amount in Canadian Dollars: ${total_dollar:.2f}")

def calcpound():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
    print("Pound Money Calculator")  # Display a title for the Pound calculator.
    print("Enter the number of each Pound Bill/Coin denomination:")  # Prompt the user to input the number of each Pound denomination.
    
    try:
        # Input the quantity of each Pound bill/coin denomination.
        onep = int(input("Number of 1p coins: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        twop = int(input("Number of 2p coins: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        fivep = int(input("Number of 5p coins: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        tenp = int(input("Number of 10p coins: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        twentyp = int(input("Number of 20p coins: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        fiftyp = int(input("Number of 50p coins: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        one = int(input("Number of £1 coins: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        two = int(input("Number of £2 coins: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        five = int(input("Number of £5 bills: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        ten = int(input("Number of £10 bills: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        twenty = int(input("Number of £20 bills: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        fifty = int(input("Number of £50 bills: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        hundred = int(input("Number of £100 bills: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        calcpound()  # Call the function again to re-enter Pound values if there's invalid input.

    # Calculate the total amount in Pounds based on user input.
    total_pounds = (onep * 0.01) + (twop * 0.02) + (fivep * 0.05) + (tenp * 0.10) + (twentyp * 0.25) + (fiftyp * 0.50) + \
                   (one * 1) + (two * 2) + (five * 5) + (ten * 10) + \
                   (twenty * 20) + (fifty * 50) + (hundred * 100)
    
    # Display the total amount in Pounds with 2 decimal places.
    print(f"\nTotal amount in Pounds: ${total_pounds:.2f}")

# Main loop that allows the user to choose a currency calculator or exit.
while True:
    print("1. Choose currency.")
    print("2. Exit.")
    
    selection = input("Selection: ")  # Prompt the user to select an option.

    if selection == "1":
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        print("1. Euro")
        print("2. Dollar")
        print("3. Canadian Dollar")
        print("4. Pounds")
        
        selection = input("Selection: ")  # Prompt the user to select a currency calculator.

        if selection == "1":
            calceuro()  # Call the Euro calculator function.
        elif selection == "2":
            calcdollar()  # Call the Dollar calculator function.
        elif selection == "3":
            calccaddollar()  # Call the Canadian Dollar calculator function.
        elif selection == "4":
            calcpound()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
            print("Invalid selection.")  # Display an error message for an invalid selection.
    
    elif selection == "2":
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        break  # Exit the program.
    
    else:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        print("Invalid selection.")  # Display an error message for an invalid selection.
