from random import randint

number = randint(0,100)
guess = int(input("Guess the number(0-100): "))
minimum = 0
maximum = 100
total = 1
while guess != number:
    if guess < number:
        minimum = guess
    else:
        maximum = guess
    print(f"Min: {minimum}\n"
          f"Max: {maximum}")
    total += 1
    if guess < number:
        guess = int(input("Guess higher: "))
    else:
        guess = int(input("Guess lower: "))
print(f"Congratulations, you've guessed the number {number} correctly after {total} tries!")