# Barter Value Calculator

def calculate_trade_value(item1, value1, item2, value2):
    """
    Compares the perceived values of two items in a barter trade.
    Returns whether the trade is fair or not.
    """
    print(f"\nYou want to trade {item1} (Value: {value1}) for {item2} (Value: {value2})\n")
    
    if value1 == value2:
        print("This trade is perfectly fair!")
    elif value1 > value2:
        print(f"The trade favors the person trading {item1}. Consider balancing the trade.")
    else:
        print(f"The trade favors the person trading {item2}. Consider balancing the trade.")

# User input
print("Welcome to the Barter Value Calculator!")
item1 = input("Enter the first item: ")
value1 = float(input(f"Enter the value of {item1} (numeric only): "))
item2 = input("Enter the second item: ")
value2 = float(input(f"Enter the value of {item2} (numeric only): "))

# Calculate and display results
calculate_trade_value(item1, value1, item2, value2)
