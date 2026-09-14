# Introduction/greeting
print("Hello.  You are about to take a 5-question quiz.")

# Print blank line
print()

#Initialize score variable to 0
score = 0

# Ask question 1 and read in user input
answer_1 = input("1) What is the capital of France? ").lower().strip()
# If the user answers "Paris", tell them they are correct
if answer_1 == "paris":
    print("Correct!")
    # Add one to the score variable for the correct answer
    score += 1
# If the user answers anything other than "Paris",
# tell them the answer is incorrect and give them
# the correct answer
else:
    print("Incorrect.  The answer is \"Paris\".")
# Print blank line
print()

# Ask question 2 and read in user input
answer_2 = input("2) How many planets are in our solar system?"
                 " (Enter your answer as an integer) ").lower().strip()
# If the user answers "8", tell them they are correct
if answer_2 == "8":
    print("Correct!")
    # Add 1 to score variable for correct answer
    score += 1
# If user answers anything other than "8", tell them
# the answer is incorrect and give them the correct
# answer
else:
    print("Incorrect.  The answer is 8.")
#print blank line
print()

# Ask question 3 and read in user input
answer_3 = input("3) What year did World War II end?"
                     " (Enter your answer as an integer.) ").strip()
# If the user answers "1945", tell them they are correct
if answer_3 == "1945":
    print("Correct!")
    # Add 1 to score variable for correct answer
    score += 1
# If user answers anything other than "1945", tell
# them the answer is incorrect and give them the
# correct answer
else:
    print("Incorrect.  The answer is 1945.")
# print blank line
print()

# Ask question 4 and read in user input
answer_4 = input("4) What is the largest ocean on Earth? ").lower().strip()
# If the user answers "Pacific" or "Pacific Ocean", tell them
# the answer is correct
if answer_4 == "pacific" or answer_4 == "pacific ocean":
    print("Correct!")
    # Add 1 to score variable for correct answer
    score += 1
# If user enters anything else, tell them the answer is
# incorrect and give them the correct answer
else:
    print("Incorrect.  The answer is \"Pacific\".")
# Print blank line
print()

# Ask question 5 and read in user input
answer_5 = input("5) How many sides does a hexagon have?"
                 " (Enter your answer as an integer) ").strip()
# If the user answers "6", tell them the answer is correct
if answer_5 == "6":
    print("Correct!")
    # Add 1 to score variable for correct answer
    score += 1
# If the user enters anything other than "6", tell them
# the answer is incorrect and give them the correct
# answer
else:
    print("Incorrect.  The answer is 6.")
# Print blank line
print()
# Display the user's quiz score.
print(f"You scored {score} out of 5 ({(score/5) * 100:.0f}%) on the quiz.")



