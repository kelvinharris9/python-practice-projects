import json
# Initialize global variables
entries = []
total_income = 0.0
total_expenses = 0.0
balance = total_income - total_expenses

# Heading for start of program
def heading():
    print("----------Budget Tracker----------")

# Function that attempts to load all entries
def load_budget():
    # Allow this function to modify these global variables
    global entries, total_income, total_expenses, balance
    try:
        with open("budget.json", "r") as f:
            entries = json.load(f)
            # Adjust totals
            for entry in entries:
                if entry["type"] == "income":
                    total_income += entry["amount"]
                    balance = total_income - total_expenses
                elif entry["type"] == "expense":
                    total_expenses += entry["amount"]
                    balance = total_income - total_expenses
    except FileNotFoundError:
        entries = [] # Keep entries as an empty list if file not found

# Function that saves entries list to .json file
def save_budget():
    with open("budget.json", "w") as f:
        json.dump(entries, f)

# Function that adds income to budget tracker
def add_income():
    # Allow this function to modify these global variables
    global entries, total_income, balance
    # Prompt user to enter details
    description = input("Enter the source of income.  (e.g. Paycheck)\n"
                        "Type here -> ").title().strip()
    amount = round(float(input("Enter the amount of income.  (Exclude dollar sign)\n"
                   "Type here -> ")), 2)
    # Append entry to list
    entries.append({"description": description, "type": "income", "amount": amount})
    # Adjust totals
    total_income += amount
    balance = total_income - total_expenses
    # Save to file
    save_budget()

# Function that adds an expense to budget tracker
def add_expense():
    # Allow this function to modify these global variables
    global entries, total_expenses, balance
    # Prompt user to enter details
    description = input("Enter the name of the expense.  (e.g. Groceries)\n"
                        "Type here -> ").title().strip()
    amount = round(float(input("Enter the amount of the expense.  (Exclude dollar sign)\n"
                   "Type here -> ")), 2)
    # Append entry to list
    entries.append({"description": description, "type": "expense", "amount": amount})
    # Adjust totals
    total_expenses += amount
    balance = total_income - total_expenses
    # Save to file
    save_budget()

# Function that removes entry
def delete_entry():
    # Allow this function to modify these global variables
    global entries, balance, total_expenses, total_income
    # Ask user which entry to delete
    entry_to_delete = input("Enter the expense or source of income you wish to delete.\n"
                            "Type here -> ").title().strip()
    print()
    # Adjust totals
    for entry in entries:
        if entry_to_delete == entry["description"]:
            if entry["type"] == "income":
                total_income -= entry["amount"]
                balance = total_income - total_expenses
                entries.remove(entry)
            elif entry["type"] == "expense":
                total_expenses -= entry["amount"]
                balance = total_income - total_expenses
                entries.remove(entry)
    save_budget()

# Function that displays balance to user
def view_balance():
    print(f"Balance: ${balance:,.2f}\n\n")

# Function that displays all entries
def view_all_entries():
    if entries:
        for entry in entries:
            print(f"Description: {entry["description"]}\n"
                  f"Type: {entry["type"]}\n"
                  f"Amount: ${entry["amount"]:,.2f}\n\n")
    else:
        print("You currently have no entries.\n\n")

# Function that displays menu to user
def menu():
    while True:
        user_choice = input("What would you like to do? (Enter number)\n"
                            "1) Add income\n"
                            "2) Add expense\n"
                            "3) Delete entry\n"
                            "4) View balance\n"
                            "5) View all entries\n"
                            "6) Quit\n"
                            "Type here ->  ")
        print()
        # Peform action of user choice
        if user_choice == "1":
            add_income()
        elif user_choice == "2":
            add_expense()
        elif user_choice == "3":
            delete_entry()
        elif user_choice == "4":
            view_balance()
        elif user_choice == "5":
            view_all_entries()
        elif user_choice == "6":
            print("Goodbye.\n")
            exit()
        else:
            print("Invalid entry.  Please try again.")

# Main function
def main():
    load_budget()
    heading()
    menu()

# Run the program only if this file is executed directly, not imported as a module
if __name__ == "__main__":
    main()