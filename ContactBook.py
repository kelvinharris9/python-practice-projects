import json

# Define function to read in contacts.json file
def load_contacts():
    try:
        with open("contacts.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}   # Return empty dict if file is not found

# Define function to display contact book heading
def heading():
    print("------Contacts------\n")

# Define function to add contacts to contact book
def add_contact(contacts):
    # Prompt user to enter new contact name/info and read them in
    new_contact = input("What is the name of the contact you wish to add.\n"
                        "Type here -> ")
    print()
    new_contact_pnum = input("What is the person's phone number.\n"
                             "Type here -> ")
    print()
    new_contact_email = input("What is the person's email address?\n"
                              "Type here -> ")
    print()
    # Assign phone and email values to corresponding key
    contacts[new_contact] = {"Phone": new_contact_pnum,
                             "Email": new_contact_email}
    save_contacts(contacts)

# Define function to display contacts to user
def view_contacts(contacts):
    print("---------Contacts---------\n")
    if not contacts:
        print("You have no contacts.\n")  # Inform user if contact list is empty
    else:
        for name, info in sorted(contacts.items()):
            print(f"Name: {name}\n"
                  f"Phone: {info["Phone"]}\n"
                  f"Email: {info["Email"]}\n\n")

# Define function to delete a contact
def delete_contact(contacts):
    # Read in name of contact user wishes to delete
    contact_to_delete = input("Which contact do you want to delete? (Enter\n"
                              "the full contact name)\n"
                              "Type here -> ")
    # Delete contact key and value from nested dict
    del contacts[contact_to_delete]
    save_contacts(contacts)

# Define function to overwrite .json file w/
# contents of contacts nested dictionary
def save_contacts(contacts):
    with open("contacts.json", "w") as f:
        json.dump(contacts, f)

# Function that displays menu to user and performs
# action of user choice
def menu():
    contacts = load_contacts()
    while True:
        user_choice = input("What would you like to do?\n"
              "1) Add a contact\n"
              "2) View contacts\n"
              "3) Delete a contact\n"
              "4) Exit\n\n"
              "Type here -> ")
        print()

        if user_choice == "1":
            add_contact(contacts)
        elif user_choice == "2":
            view_contacts(contacts)
        elif user_choice == "3":
            delete_contact(contacts)
        elif user_choice == "4":
            exit()
        else:
            print("Invalid entry.\n")

# Define main function
def main():
    heading()
    menu()

# Run this program only if it is executed directly, not imported as a module
if __name__ == "__main__":
    main()