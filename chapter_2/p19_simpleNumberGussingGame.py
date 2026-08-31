'''
create a simple number gussing game .
the user gets 10 chances to guess a number .
if the user guesses the number before 1o chances , stop asking the number from the user, say congrats and end the game.
the secret number is between 1 and 50.       
if the user never guesses the number, ask them 10 times and then end the game.
'''
import random

print("\nwelcome to the number guessing game...\nwe have a number that needs to be guessed !\nyou have 10 attempts" )
print("the secret number is betwee 1 and 50\n")

n = 1
# secret_number = 44
# instead of hardcoding the secret number we can generate a random number between 1 and 50 using random module.
secret_number = random.randint(1,50)


attempts = 10

while n <= 10:
    print(f"you have] ' {attempts} ' remaining ")
    num = int(input("Enter the guess number : "))
    if num == secret_number:
        print("Congratulation... you guessed the number...\n")
        break
    else:
        if num < secret_number:
            HorL = "higher"
        elif num > secret_number:
            HorL = "lower"
        print(f"not guessed... try {HorL} number...\n")
    print("you are failed...")
    n += 1
    attempts -= 1
print("game over")