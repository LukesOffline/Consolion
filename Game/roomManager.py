import sys
import random


class Room:
    def __init__(self):
        print("You enter a room.")

        you_find = random.randint(1, 2)
        if you_find == 1:
            rubies_found = random.randint(10, 50)
            print(f"You find {rubies_found} rubies!")
        else:
            print("You find a zombie!")

        cont_input = input("Type anything to continue, type end to exit.")
        if cont_input == "end":
            sys.exit()
