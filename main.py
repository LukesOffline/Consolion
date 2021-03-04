# This is the main game script.
import sys
import random

from Game.player import Player
from Game.monster import Monster

print("Welcome to Consolion, the open source console dungeon crawler written in Python")

selected_name = input("What will your name be?")
player = Player(selected_name)  # For now this is cosmetic mostly, it's not really in use, could be in the future.

running_game = True

while running_game:
    print("You enter a room.")

    you_find = random.randint(1, 2)
    if you_find == 1:
        rubies_found = random.randint(10, 50)
        print(f"{player.name} has found {rubies_found} rubies!")
    else:
        Monster("Zombie")

    cont_input = input("Type anything to continue, type end to exit.")
    if cont_input == "end":
        sys.exit()