import os

# Function to calculate the total value of Euro bills and coins.
import os

# Function to calculate the total value of Euro bills and coins.
def calceuro():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen (Windows: 'cls', Unix: 'clear')
    print("Euro Money Calculator")  # Display a title for the Euro calculator.
    print("Enter the number of each Euro bill/coin denomination:")  # Prompt the user to input the number of each Euro denomination.
    
    try:
        # Input the quantity of each Euro bill/coin denomination.
        one_cent = int(input("Number of 1 cent coins: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        two_cent = int(input("Number of 2 cent coins: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        five_cent = int(input("Number of 5 cent coins: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        ten_cent = int(input("Number of 10 cent coins: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        twenty_cent = int(input("Number of 20 cent coins: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        fifty_cent = int(input("Number of 50 cent coins: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        one_euro = int(input("Number of €1 coins: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        two_euro = int(input("Number of €2 coins: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        five_euro = int(input("Number of €5 bills: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        ten_euro = int(input("Number of €10 bills: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        twenty_euro = int(input("Number of €20 bills: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        fifty_euro = int(input("Number of €50 bills: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        hundred_euro = int(input("Number of €100 bills: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        two_hundred_euro = int(input("Number of €200 bills: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        five_hundred_euro = int(input("Number of €500 bills: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        calceuro()  # Call the function again to re-enter Euro values if there's invalid input.

    # Calculate the total amount in Euros based on user input.
    total_euro = (one_cent * 0.01) + (two_cent * 0.02) + (five_cent * 0.05) + (ten_cent * 0.10) + \
                (twenty_cent * 0.20) + (fifty_cent * 0.50) + (one_euro * 1) + (two_euro * 2) + \
                (five_euro * 5) + (ten_euro * 10) + (twenty_euro * 20) + (fifty_euro * 50) + \
                (hundred_euro * 100) + (two_hundred_euro * 200) + (five_hundred_euro * 500)
    
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

# Function to calculate the total value of Pound bills and coins.
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
    total_pounds = (onep * 0.01) + (twop * 0.02) + (fivep * 0.05) + (tenp * 0.10) + (twentyp * 0.20) + (fiftyp * 0.50) + \
                   (one * 1) + (two * 2) + (five * 5) + (ten * 10) + \
                   (twenty * 20) + (fifty * 50) + (hundred * 100)
    
    # Display the total amount in Pounds with 2 decimal places.
    print(f"\nTotal amount in Pounds: £{total_pounds:.2f}")

# Function to calculate the total value of Australian Dollar bills and coins.
def calcaud():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
    print("Australian Dollar Money Calculator")  # Display a title for the Australian Dollar calculator.
    print("Enter the number of each Australian Dollar Bill/Coin denomination:")  # Prompt the user to input the number of each Australian Dollar denomination.
    
    try:
        # Input the quantity of each Australian Dollar bill/coin denomination.
        onec = int(input("Number of 1 cent coins: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        twoc = int(input("Number of 2 cent coins: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        fivec = int(input("Number of 5 cent coins: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        tenc = int(input("Number of 10 cent coins: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        twentyc = int(input("Number of 20 cent coins: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        fiftyc = int(input("Number of 50 cent coins: "))
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
        calcaud()  # Call the function again to re-enter Australian Dollar values if there's invalid input.

    # Calculate the total amount in Australian Dollars based on user input.
    total_dollar = (onec * 0.01) + (twoc * 0.02) + (fivec * 0.05) + (tenc * 0.10) + (twentyc * 0.20) + (fiftyc * 0.50) + \
                   (one * 1) + (two * 2) + (five * 5) + (ten * 10) + \
                   (twenty * 20) + (fifty * 50) + (hundred * 100)
    
    # Display the total amount in Australian Dollars with 2 decimal places.
    print(f"\nTotal amount in Australian Dollars: ${total_dollar:.2f}")

# Function to calculate the total value of Japanese Yen bills and coins.
def calcyen():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
    print("Japanese Yen Money Calculator")  # Display a title for the Japanese Yen calculator.
    print("Enter the number of each Japanese Yen Bill/Coin denomination:")  # Prompt the user to input the number of each Japanese Yen denomination.
    
    try:
        # Input the quantity of each Japanese Yen bill/coin denomination.
        one_yen = int(input("Number of ¥1 coins: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        five_yen = int(input("Number of ¥5 coins: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        ten_yen = int(input("Number of ¥10 coins: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        fifty_yen = int(input("Number of ¥50 coins: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        hundred_yen = int(input("Number of ¥100 coins: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        five_hundred_yen = int(input("Number of ¥500 coins: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        
        # Input the quantity of each Japanese Yen banknote denomination.
        thousand_yen = int(input("Number of ¥1000 banknotes: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        five_thousand_yen = int(input("Number of ¥5000 banknotes: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        ten_thousand_yen = int(input("Number of ¥10,000 banknotes: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        calcyen()  # Call the function again to re-enter Japanese Yen values if there's invalid input.

    # Calculate the total amount in Japanese Yen based on user input.
    total_yen = (one_yen * 1) + (five_yen * 5) + (ten_yen * 10) + (fifty_yen * 50) + \
                (hundred_yen * 100) + (five_hundred_yen * 500) + \
                (thousand_yen * 1000) + (five_thousand_yen * 5000) + (ten_thousand_yen * 10000)
    
    # Display the total amount in Japanese Yen.
    print(f"\nTotal amount in Japanese Yen: ¥{total_yen}")

def calcchf():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
    print("Swiss Franc Money Calculator")  # Display a title for the Swiss Franc calculator.
    print("Enter the number of each Swiss Franc Bill/Coin denomination:")  # Prompt the user to input the number of each Swiss Franc denomination.
    
    try:
        # Input the quantity of each Swiss Franc bill/coin denomination.
        five_rappen = int(input("Number of 5 Rappen coins: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        ten_rappen = int(input("Number of 10 Rappen coins: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        twenty_rappen = int(input("Number of 20 Rappen coins: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        fifty_rappen = int(input("Number of 50 Rappen coins: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        one_franc = int(input("Number of 1 Franc coins: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        two_franc = int(input("Number of 2 Franc coins: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        five_franc = int(input("Number of 5 Franc bills: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        ten_franc = int(input("Number of 10 Franc bills: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        twenty_franc = int(input("Number of 20 Franc bills: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        fifty_franc = int(input("Number of 50 Franc bills: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        hundred_franc = int(input("Number of 100 Franc bills: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        two_hundred_franc = int(input("Number of 200 Franc bills: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        calcchf()  # Call the function again to re-enter Swiss Franc values if there's invalid input.

    # Calculate the total amount in Swiss Francs based on user input.
    total_chf = (five_rappen * 0.05) + (ten_rappen * 0.10) + (twenty_rappen * 0.20) + (fifty_rappen * 0.50) + \
                (one_franc * 1) + (two_franc * 2) + (five_franc * 5) + (ten_franc * 10) + \
                (twenty_franc * 20) + (fifty_franc * 50) + (hundred_franc * 100) + (two_hundred_franc * 200)
    
    # Display the total amount in Swiss Francs.
    print(f"\nTotal amount in Swiss Francs: CHF {total_chf:.2f}")

def calccnh():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
    print("Chinese Renminbi (CNH) Money Calculator")  # Display a title for the CNH calculator.
    print("Enter the number of each CNH Bill/Coin denomination:")  # Prompt the user to input the number of each CNH denomination.
    
    try:
        # Input the quantity of each CNH bill/coin denomination.
        one_fen = int(input("Number of 1 Fen coins: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        two_fen = int(input("Number of 2 Fen coins: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        five_fen = int(input("Number of 5 Fen coins: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        one_jiao = int(input("Number of 1 Jiao coins: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        five_jiao = int(input("Number of 5 Jiao coins: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        one_cnh = int(input("Number of 1 CNH coins: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        five_cnh = int(input("Number of 5 CNH coins: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        
        # Input the quantity of each CNH banknote denomination.
        one_yuan = int(input("Number of 1 Yuan banknotes: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        five_yuan = int(input("Number of 5 Yuan banknotes: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        ten_yuan = int(input("Number of 10 Yuan banknotes: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        twenty_yuan = int(input("Number of 20 Yuan banknotes: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        fifty_yuan = int(input("Number of 50 Yuan banknotes: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        one_hundred_yuan = int(input("Number of 100 Yuan banknotes: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        calccnh()  # Call the function again to re-enter CNH values if there's invalid input.

    # Calculate the total amount in Chinese Renminbi (CNH) based on user input.
    total_cnh = (one_fen * 0.01) + (two_fen * 0.02) + (five_fen * 0.05) + (one_jiao * 0.1) + \
                (five_jiao * 0.5) + (one_cnh * 1) + (five_cnh * 5) + \
                (one_yuan * 1) + (five_yuan * 5) + (ten_yuan * 10) + \
                (twenty_yuan * 20) + (fifty_yuan * 50) + (one_hundred_yuan * 100)
    
    # Display the total amount in Chinese Renminbi (CNH).
    print(f"\nTotal amount in Chinese Renminbi: CNH {total_cnh:.2f}")

def calcpln():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
    print("Polish Zloty Money Calculator")  # Display a title for the PLN calculator.
    print("Enter the number of each Polish Zloty Bill/Coin denomination:")  # Prompt the user to input the number of each PLN denomination.
    
    try:
        # Input the quantity of each Polish Zloty bill/coin denomination.
        one_grosz = int(input("Number of 1 grosz coins: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        two_grosze = int(input("Number of 2 grosze coins: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        five_groszy = int(input("Number of 5 groszy coins: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        ten_groszy = int(input("Number of 10 groszy coins: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        twenty_groszy = int(input("Number of 20 groszy coins: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        fifty_groszy = int(input("Number of 50 groszy coins: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        one_pln = int(input("Number of 1 PLN coins: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        two_pln = int(input("Number of 2 PLN coins: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        five_pln = int(input("Number of 5 PLN coins: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        ten_pln = int(input("Number of 10 PLN coins: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        twenty_pln = int(input("Number of 20 PLN banknotes: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        fifty_pln = int(input("Number of 50 PLN banknotes: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        hundred_pln = int(input("Number of 100 PLN banknotes: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        two_hundred_pln = int(input("Number of 200 PLN banknotes: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        five_hundred_pln = int(input("Number of 500 PLN banknotes: "))
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        calcpln()  # Call the function again to re-enter PLN values if there's invalid input.

    # Calculate the total amount in Polish Zloty (PLN) based on user input.
    total_pln = (one_grosz * 0.01) + (two_grosze * 0.02) + (five_groszy * 0.05) + (ten_groszy * 0.10) + \
                (twenty_groszy * 0.20) + (fifty_groszy * 0.50) + (one_pln * 1) + (two_pln * 2) + \
                (five_pln * 5) + (ten_pln * 10) + (twenty_pln * 20) + (fifty_pln * 50) + \
                (hundred_pln * 100) + (two_hundred_pln * 200) + (five_hundred_pln * 500)
    
    # Display the total amount in Polish Zloty (PLN) with 2 decimal places.
    print(f"\nTotal amount in Polish Zloty: PLN {total_pln:.2f}")

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
        print("5. Australian Dollar")
        print("6. Japanese Yen")
        print("7. Swiss Franc")
        print("8. Chinese Renminbi (CNH)")
        print("9. Polish Zloty (PLN)")
        
        selection = input("Selection: ")  # Prompt the user to select a currency calculator.

        if selection == "1":
            calceuro()  # Call the Euro calculator function.
        elif selection == "2":
            calcdollar()  # Call the Dollar calculator function.
        elif selection == "3":
            calccaddollar()  # Call the Canadian Dollar calculator function.
        elif selection == "4":
            calcpound()  # Call the Pound calculator function.
        elif selection == "5":
            calcaud()  # Call the Australian Dollar calculator function.
        elif selection == "6":
            calcyen()  # Call the Japanese Yen calculator function.
        elif selection == "7":
            calcchf()  # Call the Swiss Franc calculator function.
        elif selection == "8":
            calccnh()  # Call the Chinese Renminbi calculator function.
        elif selection == "9":
            calcpln()  # Call the Polish Zloty calculator function.
        else:
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
            print("Invalid selection.")  # Display an error message for an invalid selection.
    
    elif selection == "2":
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        break  # Exit the program.
    
    else:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen.
        print("Invalid selection.")  # Display an error message for an invalid selection.
