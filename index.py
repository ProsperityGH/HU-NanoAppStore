print(" _____ _    _____    ___                _                            _               ")
print("/  __ | |  |_   _|  / _ \              | |                          | |             ")
print("| /  \| |    | |   / /_\ \_ __  _ __   | |     __ _ _   _ _ __   ___| |__   ___ _ __")
print("| |   | |    | |   |  _  | '_ \| '_ \  | |    / _` | | | | '_ \ / __| '_ \ / _ | '__|")
print("| \__/| |____| |_  | | | | |_) | |_) | | |___| (_| | |_| | | | | (__| | | |  __| |  ")
print(" \____\_____\___/  \_| |_| .__/| .__/  \_____/\__,_|\__,_|_| |_|\___|_| |_|\___|_|  ")
print("                         | |   | |                                                  ")
print("                         |_|   |_|                                                  ")
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