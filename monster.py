import playerData


class Monster:
    def __init__(self, name, strength, health):
        self.name = name
        self.strength = strength
        self.health = health
        print(f"A {name} with a strength of {strength} has appeared!")

    def attack(self, weapon_name, weapon_damage):
        print(f"The zombie had {self.health} hp")
        self.health = self.health - weapon_damage
        print(f"You attacked it with {weapon_name}and now it has {self.health} hp")

    def enemy_attacks(self):
        playerData.playerHealth = playerData.playerHealth - self.strength
        print(f"Player has been attacked and lost {self.strength} hp, they now have {playerData.playerHealth} hp")
