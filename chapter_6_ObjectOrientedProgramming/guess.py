import random

temp = random.randint(1,10)
guess = input("Enter your number (1 - 10) :- ").strip()
guess_new = int(guess)

guess_try = 0

while True:
    if not guess_new > 1 or guess_new < 10:
            print("Enter number in range")
            break
    
    if temp.isdigit():
        temp_1 = int(temp)
    
    else:
        print("Enter valid digit")
        
    
    guess_try += 1
    
    if guess == temp_1:
        print(f"you won in {guess_try} tries")
    quit()

    if guess > temp_1:
        print("You are above")
    
    elif guess < temp_1:
        print("You are below")

print(f"you won in {guess_try} tries")
    
    
        