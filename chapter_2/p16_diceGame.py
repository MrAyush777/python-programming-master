''' write a program to simulate a roll of a dice/die
a dia has 6 faces with numbers 1 to 6. on them
the program should generate a random number between 1 and 6 and print it to the user '''

import random

while True:
    
    choice = input("press 'enter' to roll or 'q' to quit : ")
    
    if choice == '':
        num1 = random.randint(1,6)
        num2 = random.randint(1,6)
        print(f"the number on the dise is {num1, num2}")
    elif choice == 'q':
        print("thanks for playing the game...")
        break
    else:
        print("invalid input, try again...")

print("game over...")