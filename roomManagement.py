import random
import sys
from monster import Monster
import playerData


def new_room():  # This is run 24/7 basically
    x = random.randint(1, 1)

    # Curse pythons lack of switch statements
    if x == 1:
        # Room variables
        room_width = random.randint(5, 30)
        room_length = random.randint(5, 30)
        monster_chance = random.randint(1, 3)

        print(f"You have found a basic room with a length of {room_width} and a length of {room_length}")
        if monster_chance == 1:
            zombie = Monster("Zombie", 5, 10)

            while zombie.health > 0:  # Whilst zombie is alive
                attack_prompt = input("Type fight to attack it!")

                if attack_prompt == "fight":  # Combat
                    zombie.attack(playerData.sword.name, playerData.sword.damage)

                chance_of_attack = random.randint(1, 2)  # Note that death is not a thing yet.
                if chance_of_attack:
                    zombie.enemy_attacks()

            # Player gets coins for killing it
            print("You found 25 coins from killing the zombie")
            playerData.playerCoins = playerData.playerCoins + 25
        else:
            # Find coins
            coins_room = random.randint(5, 100)
            print(f"You have found {coins_room} coins.")
            playerData.playerCoins = playerData.playerCoins + coins_room
            print(f"You have {playerData.playerCoins} coins total.")
    elif x == 2:
        # Room variables
        room_width = random.randint(5, 30)
        room_length = random.randint(5, 30)
        monster_chance = random.randint(1, 3)

        print(f"You have found a basic room with a length of {room_width} and a length of {room_length}")
        if monster_chance == 1:
            zombie = Monster("Zombie", 5, 10)

            while zombie.health > 0:  # Whilst zombie is alive
                attack_prompt = input("Type fight to attack it!")

                if attack_prompt == "fight":  # Combat
                    zombie.attack(playerData.sword.name, playerData.sword.damage)

                chance_of_attack = random.randint(1, 2)  # Note that death is not a thing yet.
                if chance_of_attack:
                    zombie.enemy_attacks()

            # Player gets coins for killing it
            print("You found 25 coins from killing the zombie")
            playerData.playerCoins = playerData.playerCoins + 25
        else:
            # Find coins
            coins_room = random.randint(5, 100)
            print(f"You have found {coins_room} coins.")
            playerData.playerCoins = playerData.playerCoins + coins_room
            print(f"You have {playerData.playerCoins} coins total.")
    elif x == 3:
        # Room variables
        room_width = random.randint(5, 30)
        room_length = random.randint(5, 30)
        monster_chance = random.randint(1, 3)

        print(f"You have found a basic room with a length of {room_width} and a length of {room_length}")
        if monster_chance == 1:
            zombie = Monster("Zombie", 5, 10)

            while zombie.health > 0:  # Whilst zombie is alive
                attack_prompt = input("Type fight to attack it!")

                if attack_prompt == "fight":  # Combat
                    zombie.attack(playerData.sword.name, playerData.sword.damage)

                chance_of_attack = random.randint(1, 2)  # Note that death is not a thing yet.
                if chance_of_attack:
                    zombie.enemy_attacks()

            # Player gets coins for killing it
            print("You found 25 coins from killing the zombie")
            playerData.playerCoins = playerData.playerCoins + 25
        else:
            # Find coins
            coins_room = random.randint(5, 100)
            print(f"You have found {coins_room} coins.")
            playerData.playerCoins = playerData.playerCoins + coins_room
            print(f"You have {playerData.playerCoins} coins total.")
    elif x == 4:
        # Room variables
        room_width = random.randint(5, 30)
        room_length = random.randint(5, 30)
        monster_chance = random.randint(1, 3)

        print(f"You have found a basic room with a length of {room_width} and a length of {room_length}")
        if monster_chance == 1:
            zombie = Monster("Zombie", 5, 10)

            while zombie.health > 0:  # Whilst zombie is alive
                attack_prompt = input("Type fight to attack it!")

                if attack_prompt == "fight":  # Combat
                    zombie.attack(playerData.sword.name, playerData.sword.damage)

                chance_of_attack = random.randint(1, 2)  # Note that death is not a thing yet.
                if chance_of_attack:
                    zombie.enemy_attacks()

            # Player gets coins for killing it
            print("You found 25 coins from killing the zombie")
            playerData.playerCoins = playerData.playerCoins + 25
        else:
            # Find coins
            coins_room = random.randint(5, 100)
            print(f"You have found {coins_room} coins.")
            playerData.playerCoins = playerData.playerCoins + coins_room
            print(f"You have {playerData.playerCoins} coins total.")
    elif x == 5:
        # Room variables
        room_width = random.randint(5, 30)
        room_length = random.randint(5, 30)
        monster_chance = random.randint(1, 3)

        print(f"You have found a basic room with a length of {room_width} and a length of {room_length}")
        if monster_chance == 1:
            zombie = Monster("Zombie", 5, 10)

            while zombie.health > 0:  # Whilst zombie is alive
                attack_prompt = input("Type fight to attack it!")

                if attack_prompt == "fight":  # Combat
                    zombie.attack(playerData.sword.name, playerData.sword.damage)

                chance_of_attack = random.randint(1, 2)  # Note that death is not a thing yet.
                if chance_of_attack:
                    zombie.enemy_attacks()

            # Player gets coins for killing it
            print("You found 25 coins from killing the zombie")
            playerData.playerCoins = playerData.playerCoins + 25
        else:
            # Find coins
            coins_room = random.randint(5, 100)
            print(f"You have found {coins_room} coins.")
            playerData.playerCoins = playerData.playerCoins + coins_room
            print(f"You have {playerData.playerCoins} coins total.")
    else:
        print("Game broke lol")

    cont = input("Type to continue, type end to quit")  # At the end of the room
    if cont == "end":
        sys.exit()
