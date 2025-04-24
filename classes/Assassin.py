from Character import Character

# Assassin class (inherits from Character)
class Assassin(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)
