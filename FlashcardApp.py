import json

# Function that loads flashcards from .json file to dict
def load_flashcards():
    try:
        with open("flashcards.json", "r") as f:
            flashcards = json.load(f)
            return flashcards
    except FileNotFoundError:
        return {} # return empty dict if file not found

# Function to greet user
def greeting():
    print("Hello.  You are about to take the flashcard quiz.\n\n")

# Function that displays quiz to user and keeps score
def quiz(flashcards):
    # User score starts at 0
    user_score = 0
    # Start from question 1
    question_num = 1
    # Display each question and read in user answer
    for question, answer in flashcards.items():
        user_answer = input(f"{question_num}) {question}\n"
              f"Type here -> ").lower().strip()
        print()
        # Adjust user score if needed, increment question number
        if user_answer == answer:
            print("Correct!\n\n")
            user_score += 1
            question_num += 1
        else:
            # Display correct answer if user's answer is incorrect
            print(f"Incorrect.  The correct answer is: {answer}.\n\n")
            question_num += 1
    question_num -= 1
    display_score(user_score, question_num)

# Function to display user score
def display_score(score, num_questions):
    print(f"You scored {score} out of {num_questions} ({int((score/num_questions) * 100)}%) "
          f"on the quiz.")

# Main function
def main():
    flashcards = load_flashcards()
    greeting()
    quiz(flashcards)

# Run this program only if file is executed directly, not imported as a module
if __name__ == "__main__":
    main()