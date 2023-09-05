import os

def calceuro():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Euro Money Calculator")
    print("Enter the number of each Euro bill/coin denomination:")
    
    # Input the number of each Euro bill/coin denomination
    one = int(input("Number of €1 coins: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    two = int(input("Number of €2 coins: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    five = int(input("Number of €5 bills: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    ten = int(input("Number of €10 bills: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    twenty = int(input("Number of €20 bills: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    fifty = int(input("Number of €50 bills: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    hundred = int(input("Number of €100 bills: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    two_hundred = int(input("Number of €200 bills: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    five_hundred = int(input("Number of €500 bills: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Calculate the total amount in Euros
    total_euro = (one * 1) + (two * 2) + (five * 5) + (ten * 10) + \
                (twenty * 20) + (fifty * 50) + (hundred * 100) + \
                (two_hundred * 200) + (five_hundred * 500)
    
    # Display the total amount in Euros
    print(f"\nTotal amount in Euros: €{total_euro:.2f}")

def calcdollar():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Dollar Money Calculator")
    print("Enter the number of each Dollar Bill denomination:")
    
    # Input the number of each Dollar bill denomination
    one = int(input("Number of $1 bills: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    two = int(input("Number of $2 bills: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    five = int(input("Number of $5 bills: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    ten = int(input("Number of $10 bills: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    twenty = int(input("Number of $20 bills: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    fifty = int(input("Number of $50 bills: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    hundred = int(input("Number of $100 bills: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Calculate the total amount in Dollars
    total_dollar = (one * 1) + (two * 2) + (five * 5) + (ten * 10) + \
                (twenty * 20) + (fifty * 50) + (hundred * 100)
    
    # Display the total amount in Dollars
    print(f"\nTotal amount in Dollars: ${total_dollar:.2f}")

def calccaddollar():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Canadian Dollar Money Calculator")
    print("Enter the number of each Canadian Dollar Bill/Coin denomination:")
    
    # Input the number of each Canadian Dollar coin denomination
    nickel = int(input("Number of 5 cent coins: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    dime = int(input("Number of 10 cent coins: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    quarter = int(input("Number of 25 cent coins: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    fifty_cent = int(input("Number of 50 cent coins: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    one = int(input("Number of $1 coins: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    two = int(input("Number of $2 coins: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    five = int(input("Number of $5 bills: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    ten = int(input("Number of $10 bills: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    twenty = int(input("Number of $20 bills: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    fifty = int(input("Number of $50 bills: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    hundred = int(input("Number of $100 bills: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Calculate the total amount in Canadian Dollars
    total_dollar = (nickel * 0.05) + (dime * 0.10) + (quarter * 0.25) + (fifty_cent * 0.50) + \
                   (one * 1) + (two * 2) + (five * 5) + (ten * 10) + \
                   (twenty * 20) + (fifty * 50) + (hundred * 100)
    
    # Display the total amount in Canadian Dollars
    print(f"\nTotal amount in Canadian Dollars: ${total_dollar:.2f}")


while True:
    print("1. Choose currency.")
    print("2. Exit.")
    
    selection = input("Selection: ")

    if selection == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("1. Euro")
        print("2. Dollar")
        print("3. Canadian Dollar")

        selection = input("Selection: ")

        if selection == "1":
            calceuro()
        elif selection == "2":
            calcdollar()
        elif selection == "3":
            calccaddollar()
        else:
            print("Invalid selection.")
    
    elif selection == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        break
    
    else:
        print("Invalid selection.")
