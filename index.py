print(" _____ _    _____ _              ")
print("/  __ | |  |_   _| |             ")
print("| /  \| |    | | | |__   _____  _")
print("| |   | |    | | | '_ \ / _ \ \/ ")
print("| \__/| |____| |_| |_) | (_) >  <")
print(" \____\_____\___/|_.__/ \___/_/\_")
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