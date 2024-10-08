import random

def hangman(woord):
    fouten = 0
    hangendeMan = ["",          # De hangende man die wordt geprint
              "__________       ",
              "|        |      ",
              "|        |      ",
              "|        0      ",
              "|       /|\     ",
              "|       / \     ",
              "|               "
              ]
    rletters = list(woord)
    bord = ["__"] * len(woord) # _ _ in het spel betekent een leeg vak
    gewonnen = False

    print("Welkom bij Galgje")

    while fouten < len(hangendeMan) - 1:
        print("\n")
        bericht = "Raad een letter: "
        letter = input(bericht)

        if letter in rletters:
            cind = rletters.index(letter)
            bord[cind] = letter
            rletters[cind] = '$'
        else:
            fouten += 1

        print((" ".join(bord)))
        e = fouten + 1 
        print("\n".join(hangendeMan[0: e]))
        
        if "__" not in bord: #Als het woord volledig is beschreven stopt het spel en wint de speler
            print("Je wint!")
            print(" ".join(bord))
            gewonnen = True
            break

    if not gewonnen:
        print("\n".join(hangendeMan[0: fouten])) # Toon de volledige hangman
        print("Je verliest! Het woord was {}.".format(woord))

def startGame():
    woorden = ["kat", "hond", "vogel", "vis", "olifant"] # Woorden die willekeurig worden gebruikt in het spel
    woord = random.choice(woorden)
    hangman(woord)
