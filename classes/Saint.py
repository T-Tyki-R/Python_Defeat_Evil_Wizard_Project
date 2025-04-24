from Character import Character

# Saint class (inherits from Character)
class Saint(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)
