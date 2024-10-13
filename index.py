print("  _____  _     _____    ___  ______ ______   _____  _____  _____ ______  _____ ")
print("/  __ \| |   |_   _|  / _ \ | ___ \| ___ \ /  ___||_   _||  _  || ___ \|  ___|")
print("| /  \/| |     | |   / /_\ \| |_/ /| |_/ / \ `--.   | |  | | | || |_/ /| |__ ")
print("| |    | |     | |   |  _  ||  __/ |  __/   `--. \  | |  | | | ||    / |  __| ")
print("| \__/\| |_____| |_  | | | || |    | |     /\__/ /  | |  \ \_/ /| |\ \ | |___ ")
print(" \____/\_____/\___/  \_| |_/\_|    \_|     \____/   \_/   \___/ \_| \_|\____/ ")
print("")

import randomNumber as rNumb
import hangman as hM

def randomNumber():
    print("1: Random Number Generator")
    print("2: Hangman")

    keuze = int(input("GEEF OP WELKE OPTIE JE WILT KIEZEN! "))

    match keuze:
        case 1:
            rNumb.startGame()
        case 2:
            hM.startGame()

randomNumber()