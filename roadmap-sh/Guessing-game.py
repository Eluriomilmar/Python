from random import randint

number = randint(0,100)
guess = int(input("Guess the number(0-100): "))
min = 0
max = 100
total = 1
while guess != number:
    if guess < number:
        min = guess
    else:
        max = guess
    print(f"Min: {min}\n"
          f"Max: {max}")
    total += 1
    if guess < number:
        guess = int(input("Guess higher: "))
    else:
        guess = int(input("Guess lower: "))
print(f"Congratulations, you've guessed the number {number} correctly after {total} tries!")