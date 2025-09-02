#Python quiz game

questions = ("Question 1: How many elements are i nthe periodic table?",
             "Question 2: ",
             "Question 3: ",
             "Question 4: ",
             "Question 5: ")

options = (("A. 118", "B. 116", "C. 117", "D. 119"),
           ("A. Chicken", "B. Platipus", "C. Whale", "D. Ostrich"),
           ("A. Ogygen", "B. Carbon", "C. Hydrogen", "D. Nitrogen"),
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
