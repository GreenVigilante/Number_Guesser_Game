import random

number = random.randint(0,10000)
tries = 0
guessed = False
while not guessed:
    guess = int(input("Guess the number: "))
    tries +=1
    if guess > number:
        print(f"The number is less than {guess}")
    elif guess < number:
        print(f"The number is greater than {guess}")
    elif guess == number:
        print("Congrats you won!")
        guessed = True
