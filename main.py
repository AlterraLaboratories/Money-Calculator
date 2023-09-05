import os

# Function to calculate total money in Euros
def calculate_total_money_euro():
    print("Euro Money Calculator")
    print("Enter the number of each Euro bill/coin denomination:")
    
    # Input the number of each Euro bill/coin denomination
    os.system('cls' if os.name == 'nt' else 'clear')    
    one_euro = int(input("Number of €1 coins: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    two_euros = int(input("Number of €2 coins: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    five_euros = int(input("Number of €5 bills: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    ten_euros = int(input("Number of €10 bills: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    twenty_euros = int(input("Number of €20 bills: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    fifty_euros = int(input("Number of €50 bills: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    hundred_euros = int(input("Number of €100 bills: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    two_hundred_euros = int(input("Number of €200 bills: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    five_hundred_euros = int(input("Number of €500 bills: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Calculate the total amount in Euros
    total_euro = (one_euro * 1) + (two_euros * 2) + (five_euros * 5) + (ten_euros * 10) + \
                (twenty_euros * 20) + (fifty_euros * 50) + (hundred_euros * 100) + \
                (two_hundred_euros * 200) + (five_hundred_euros * 500)
    
    # Display the total amount in Euros
    print(f"\nTotal amount in Euros: €{total_euro:.2f}")

# Call the function to calculate total money in Euros
calculate_total_money_euro()
