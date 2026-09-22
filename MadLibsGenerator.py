# Initialize global variables
user_noun = ""
user_verb = ""
user_adjective = ""
user_place = ""

# Define function to read in user input
def get_input():
    # Allows this function to modify each of the global variables listed
    global user_noun
    global user_verb
    global user_adjective
    global user_place

    # Prompt user to enter the words
    print("Enter a word for each figure of speech listed.")
    print()

    # Read in user input
    user_noun = input("Noun: ")
    user_verb = input("Verb: ")
    user_adjective = input("Adjective: ")
    user_place = input("Place: ")
    print()

# Define function that prints the story using user input
def print_story():
    print("Your story:")
    print(f"One day a {user_adjective} {user_noun} {user_verb} into "
          f"{user_place} and nobody knew what to do.")

# Define main function
def main():
    get_input()
    print_story()

# Call main function to run only if this program is executed directly, not imported as a module
if __name__ == "__main__":
    main()