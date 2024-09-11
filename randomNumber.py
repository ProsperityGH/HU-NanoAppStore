import random
number= random.randint(1, 100)
antwoord = input("Guess the number between 1 and 100: ")

for i in range(10):
    if int(userInput) == number:
        print("You have guessed the number correctly!")
        break
    else: 
        antwoord = input("Try again: ")