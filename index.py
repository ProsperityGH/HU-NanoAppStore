print(" /$$   /$$  /$$$$$$  /$$   /$$  /$$$$$$         /$$$$$$  /$$$$$$$  /$$$$$$$   /$$$$$$  /$$$$$$$$ /$$$$$$  /$$$$$$$  /$$$$$$$$        /$$$$$$  /$$$$$$$  /$$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$  /$$   /$$ /$$$$$$$$/")
print("| $$$ | $$ /$$__  $$| $$$ | $$ /$$__  $$       /$$__  $$| $$__  $$| $$__  $$ /$$__  $$|__  $$__//$$__  $$| $$__  $$| $$_____/       /$$__  $$| $$__  $$| $$__  $$| $$__  $$ /$$__  $$ /$$__  $$| $$  | $$|__  $$__/")
print("| $$$$| $$| $$  \ $$| $$$$| $$| $$  \ $$      | $$  \ $$| $$  \ $$| $$  \ $$| $$  \__/   | $$  | $$  \ $$| $$  \ $$| $$            | $$  \ $$| $$  \ $$| $$  \ $$| $$  \ $$| $$  \ $$| $$  \__/| $$  | $$   | $$   ")
print("| $$ $$ $$| $$$$$$$$| $$ $$ $$| $$  | $$      | $$$$$$$$| $$$$$$$/| $$$$$$$/|  $$$$$$    | $$  | $$  | $$| $$$$$$$/| $$$$$         | $$  | $$| $$$$$$$/| $$  | $$| $$$$$$$/| $$$$$$$$| $$      | $$$$$$$$   | $$   ")
print("| $$  $$$$| $$__  $$| $$  $$$$| $$  | $$      | $$__  $$| $$____/ | $$____/  \____  $$   | $$  | $$  | $$| $$__  $$| $$__/         | $$  | $$| $$____/ | $$  | $$| $$__  $$| $$__  $$| $$      | $$__  $$   | $$   ")
print("| $$\  $$$| $$  | $$| $$\  $$$| $$  | $$      | $$  | $$| $$      | $$       /$$  \ $$   | $$  | $$  | $$| $$  \ $$| $$            | $$  | $$| $$      | $$  | $$| $$  \ $$| $$  | $$| $$    $$| $$  | $$   | $$   ")
print("| $$ \  $$| $$  | $$| $$ \  $$|  $$$$$$/      | $$  | $$| $$      | $$      |  $$$$$$/   | $$  |  $$$$$$/| $$  | $$| $$$$$$$$      |  $$$$$$/| $$      | $$$$$$$/| $$  | $$| $$  | $$|  $$$$$$/| $$  | $$   | $$   ")
print("|__/  \__/|__/  |__/|__/  \__/ \______/       |__/  |__/|__/      |__/       \______/    |__/   \______/ |__/  |__/|________/       \______/ |__/      |_______/ |__/  |__/|__/  |__/ \______/ |__/  |__/   |__/   ")

import randomNumber as rNumb
import hangman as hM

def randomNumber():
    print("1: Random Number Generator")
    print("2: Hangman")

    keuze = int(input("GEEF OP WELKE OPTIE JE WILT KIEZEN!"))

    match keuze:
        case 1:
            rNumb.startGame()
        case 2:
            hM.startGame()

randomNumber()