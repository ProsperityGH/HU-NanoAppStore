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
    
    try:
        keuze = int(input("GEEF OP WELKE OPTIE JE WILT KIEZEN! "))
        
        match keuze:
            case 1:
                rNumb.startGame()
            case 2:
                hM.startGame()
            case _:
                print("Ongeldige keuze, kies 1 of 2.")
    except ValueError:
        print("Ongeldige invoer! Voer een getal in.")
    except Exception as e:
        print(f"Er is een fout opgetreden: {e}")


randomNumber()