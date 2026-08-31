import random

print("Welcome to 'Game of Guess' !!! ")

while True:
    first = input("Enter your Starting  range:- ").strip()
    if not first.isdigit():
        print("Enter the digit")
        continue

    else:
        first = int(first)
        break

while True:
    last = input("Enter your Ending range:- ").strip()
    if not last.isdigit():
        print("Enter the digit")
        continue

    last = int(last)

    if last < first:
        print("The end must be greater than starting !!!")
        continue
    else:
        print("Both Numbers are Entered")
        break

temp = random.randint(first,last)

guess_try = 0

while True:
    guess = input("Enter you number for guess or Enter 'q'  or 'Q' for quit:- ").lower().strip()
    if guess == 'q':
        print("You are Quitting...")
        quit()
    if not guess.isdigit():
        print("Please Enter Digit")
        continue

    else:
        guess = int(guess)

    guess_try += 1
    if guess == temp:
        print(f"You Guessed it in {guess_try} attempts.")
        break

    elif guess < first:
        print("You are above")
    else: 
        print("You are below")