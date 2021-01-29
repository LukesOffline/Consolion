# Luke's first Python project, a console based dungeon crawler.
from roomManagement import *
GameRunning: bool = False

# Game Intro
print("Welcome to Consolion type anything to continue!")
input()

# Run the game
GameRunning = True

# Game is now running
while GameRunning:
    new_room()
