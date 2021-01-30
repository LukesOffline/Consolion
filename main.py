# This is the main game script.
from Game.player import Player
from Game.roomManager import Room

print("Welcome to Consolion, the open source console dungeon crawler written in Python")

selected_name = input("What will your name be?")
player = Player(selected_name)

running_game = True

while running_game:
    Room()
