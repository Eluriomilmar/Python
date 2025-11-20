#Python quiz game

questions = ("Question 1: How many elements are in the periodic table?",
             "Question 2: Which animal lays the largest eggs?",
             "Question 3: What is the most abundant gas in Earth's atmosphere?",
             "Question 4: How many bones are in the human body?",
             "Question 5: Which planet in the solar system is the hottest?")

options = (("A. 118", "B. 116", "C. 117", "D. 119"),
           ("A. Chicken", "B. Platipus", "C. Whale", "D. Ostrich"),
           ("A. Oxygen", "B. Carbon", "C. Hydrogen", "D. Nitrogen"),
           ("A. 206", "B. 207", "C. 205", "D. 208"),
           ("A. Mercury", "B. Earth", "C. Venus", "D. Mars"))

answers = ("A", "D", "D", "A", "C")
question_num = 0
score = 0

for question in questions:
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("\nEnter A, B, C or D.: ").upper()
    if guess == answers[question_num]:
        question_num += 1
        score += 1
    else:
        break
print(f"\nThe game has ended with a score of {score}.")
