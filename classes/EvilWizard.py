from Character import Character

# Evil Wizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=175, attack_power=20)

    def regenerate(self):
        health_regen = self.health * .1  # Regenerate 10% of health
        # Check if the wizard's health is below a certain threshold before regenerating
        if self.health < 160 and self.healh + health_regen < 160: 
            self.health += health_regen
            print(f"{self.name} regenerates {health_regen} health! Current health: {self.health}")
        else:
            # If health is above the threshold, set it to max health = (160)
            self.health = 160
            print(f"{self.name} has maxed out health! Current health: {self.health}")

