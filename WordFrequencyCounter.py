# Initialize global variables
words = []
counts = {}

# Function to read in .txt file
def read_in_file():
    # Allows this function to modify global variable words
    global words
    # Prompt user to enter file name
    filename = input("Hello, friend!  Enter the exact name of the file you wish to upload.\n"
                     "(Ensure the file is in the same folder as this Python file).\n"
                     "Type here -> ").strip()
    print("\n")
    # Split string of text from .txt file into a list
    try:
        with open(filename, "r", encoding="utf-8") as f:
            words = [word.strip(".,;:!?-") for word in f.read().lower().split()]
        return True
    # Inform user if file is not found
    except FileNotFoundError:
        print("File not found.\n")
        return False

# Function to parse list of words from .txt file
def parse_list():
    # Allow this function to modify global variable counts
    global counts
    for word in words:
        # Skip if not a word (for example, a loose hyphen)
        if not word:
            continue
        # Count appearances of each word
        if word in counts:
                counts[word] += 1
        else:
                counts[word] = 1

# Function to display word counts to user
def display_counts():
    # Separate and sort 10 most frequent words in .txt file into separate list
    top_10 = sorted(counts.items(), key=lambda item: item[1], reverse=True)[:10]
    print("Top 10 Most Frequent Words")
    print("-------------------------------")
    print("Word   |   Count\n")
    for word, count in top_10:
        print(f"{word.title():<11}{count:,}")

# Main function
def main():
    # After executing main function, continue only if .txt file is found
    if read_in_file():
        parse_list()
        display_counts()

# Run program only if file is executed directly, not imported as a module
if __name__ == "__main__":
    main()
