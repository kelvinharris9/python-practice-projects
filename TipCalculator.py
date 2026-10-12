# Initialize global variables
bill_amount = 0
tip_percentage = -1
tip_amount = 0
total_amount = 0

# Define function to greet user
def greeting():
    print("Hello.  I am Skip the Tip Calculator.\n")

# Define function to read in dollar amount of the bill from user input
def enter_amount():
    # Allow this function to modify global bill_amount variable
    global bill_amount
    while bill_amount <= 0:
        # Prompt user to enter bill amount and read in user input
        bill_amount = float(input("Enter bill amount greater than 0 (for example, \"82.67\") -> "))
        print()

# Define function to read in percentage user wants to tip
def enter_tip_percentage():
    # Allow this function to modify global tip_percentage variable
    global tip_percentage
    while not (tip_percentage >= 0):
        # Prompt user to enter tip amount as a percentage
        tip_percentage = float(input("Enter the percentage of the bill you want to "
                                     "tip (for example, \"20\") -> "))
        print()

# Define function to calculate tip and total amounts
def calculations():
    # Allow this function to modify global variables tip_amount and total_amount
    global tip_amount, total_amount
    # Calculate tip amount
    tip_amount = float(bill_amount * (tip_percentage / 100.0))
    # Calculate total amount
    total_amount = round(bill_amount + tip_amount, 2)

# Define function to display tip and total amounts
def display_amounts():
    print(f"You have chosen to tip ${tip_amount:.2f}.")
    print(f"Your total after the tip is ${total_amount:.2f}.")

# Define main function
def main():
    greeting()
    enter_amount()
    enter_tip_percentage()
    calculations()
    display_amounts()

# Run this program only if it is executed directly, not imported as a module
if __name__ == "__main__":
    main()