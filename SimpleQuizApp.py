# Initialize user_score variable
user_score = 0
#Introduction/greeting function
def greeting():
    # Introduction/greeting
    print("Hello.  You are about to take a 5-question quiz.")
    # Print blank line
    print()

# Function to increment the user score variable
def update_score():
    # Allow this function to modify the global user_score variable
    global user_score
    # Increment global user_score variable
    user_score += 1

# Function to ask question and read in user answer
def ask_question(question, correct_answer):
    # Ask the question
    print(question)
    # Read in user's answer
    user_answer = input("Your answer: ").title().strip()
    if isinstance(correct_answer, tuple):
        if user_answer in correct_answer:
            # Tell the user the answer is correct
            print("Correct!")
            update_score()
        # Otherwise...
        else:
            # Tell the user the answer is incorrect and tell them
            # the correct answer
            print(f"Incorrect.  The correct answer is {correct_answer[0]}.")
    else:
        if user_answer == correct_answer:
            # Tell the user the answer is correct
            print("Correct!")
            update_score()
        # Otherwise...
        else:
            # Tell the user the answer is incorrect and tell them
            # the correct answer
            print(f"Incorrect.  The correct answer is {correct_answer}.")
    # Print blank line
    print()

def display_user_score():
    # Display user's quiz score
    print(f"You scored {user_score} out of 5 ({(user_score/5) * 100:.0f}%) on the quiz.")

# Define the main function
def main():
    greeting()

    # Ask all 5 quiz questions
    ask_question("1) What is the capital of France?", "Paris")
    ask_question("2) How many planets are in our solar system?", ("8", "Eight"))
    ask_question("3) What year did World War II end? (enter "
                 "your answer as an integer)", "1945")
    ask_question("4) What is the largest ocean on Earth?",
                 ("Pacific", "Pacific Ocean", "The Pacific Ocean", "The Pacific"))
    ask_question("5) How many sides does a hexagon have?", ("6", "Six"))

    display_user_score()

# Run the program only if this file is executed directly, not imported as a module
if __name__ == "__main__":
    main()