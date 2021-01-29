class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
        print(f"Picked up {name} with a damage of {damage}")