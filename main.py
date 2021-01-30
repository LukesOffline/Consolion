# This is the main game script.
from Game.player import Player

game_running = False

print("Welcome to Consolion, the open source console dungeon crawler written in Python")
selected_name = input("What will your name be?")
player = Player(selected_name)
game_running = True

if game_running:
    print("Game running")