from random import randrange

num = randrange(1, 101)

tries = 0
guess = 0

while guess != num:

    guess = int (input("Guess a value from 1 to 100: "))

    if guess < num:
        print("Too low, please try again")
        tries += 1
    if guess > num:
        print("Too high, please try again")
        tries += 1
    if guess == num:
        print(f"{num} is the correct answer")
        tries += 1
print(f"It took you {tries} tries to get the correct answer")